# encoding: utf-8
import datetime
import importlib
import logging
import json
import os
import sys
import yaml
from .util import isstr
from nose.tools import set_trace
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import (
    create_engine,
    Binary,
    Boolean,
    Column,
    Integer,
    Unicode,
    DateTime,
    ForeignKey,
)
from sqlalchemy.exc import (
    IntegrityError
)
from sqlalchemy.orm import (
    backref,
    relationship,
)
from sqlalchemy.orm.exc import (
    NoResultFound,
    MultipleResultsFound,
)
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base


class InvalidPost(Exception):
    """There was a problem creating a Post which implies that any
    Post objects created are invalid.
    """

TIME_FORMAT = "%Y-%m-%d %H:%M"

def _now():
    """The current time.

    I've moved this into a function so I can test out whether
    local time or UTC is better for this purpose.
    """
    #return datetime.datetime.now()
    return datetime.datetime.utcnow()

Base = declarative_base()
        

def create(db, model, create_method='',
           create_method_kwargs=None,
           **kwargs):
    """Create a single model object."""
    kwargs.update(create_method_kwargs or {})
    created = getattr(model, create_method, model)(**kwargs)
    db.add(created)
    db.flush()
    return created, True

def get_one(db, model, on_multiple='error', **kwargs):
    """Gets an object from the database based on its attributes.

    :return: object or None
    """
    q = db.query(model).filter_by(**kwargs)
    try:
        return q.one()
    except MultipleResultsFound as e:
        if on_multiple == 'error':
            raise e
        elif on_multiple == 'interchangeable':
            # These records are interchangeable so we can use
            # whichever one we want.
            #
            # This may be a sign of a problem somewhere else. A
            # database-level constraint might be useful.
            q = q.limit(1)
            return q.one()
    except NoResultFound:
        return None


def get_one_or_create(db, model, create_method='',
                      create_method_kwargs=None,
                      **kwargs):
    """Get a single model object. If it doesn't exist, create it."""
    one = get_one(db, model, **kwargs)
    if one:
        return one, False
    else:
        try:
            # These kwargs are supported by get_one() but not by create().
            get_one_keys = ['on_multiple', 'constraint']
            for key in get_one_keys:
                if key in kwargs:
                    del kwargs[key]
            obj = create(db, model, create_method, create_method_kwargs, **kwargs)
            return obj
        except IntegrityError as e:
            logging.info(
                "INTEGRITY ERROR on %r %r, %r: %r", model, create_method_kwargs, 
                kwargs, e)
            return db.query(model).filter_by(**kwargs).one(), False


def engine(filename):
    """Return an engine for and database connection to the
    SQLite database at `filename`.
    """
    engine = create_engine('sqlite:///%s' % filename, echo=False)
    Base.metadata.create_all(engine)
    return engine, engine.connect()    
        
def production_session(filename):
    """Get a database connection to the SQLite database at `filename`."""
    e, connection = engine(filename)
    session = Session(connection)
    return session


class BotModel(Base):
    __tablename__ = 'bots'
    id = Column(Integer, primary_key=True)

    # The name of the directory containing the bot's configuration and
    # code.
    name = Column(Unicode)

    # If this is set, the bot will not post anything until this time.
    next_post_time = Column(DateTime)

    # The bot's implementation may store a backlog of unscheduled
    # posts in this field.
    _backlog = Column(Unicode, name='backlog')
    
    # The bot's implementation may store anything it wants in this field
    # to keep track of state between posts.
    _state = Column(Unicode, name="state")

    # The last time update_state() was called.
    last_state_update_time = Column(DateTime)
    
    posts = relationship('Post', backref='bot')
    
    @property
    def log(self):
        return logging.getLogger(self.name)
   
    @classmethod
    def from_directory(cls, _db, directory, defaults=None):
        """Load bot code from `directory`, and find or create the
        corresponding BotModel object.

        Note that the parent of `directory` must be in sys.path

        :param defaults: A set of default configuration items that can
        fill in when the bot configuration is missing something.

        :return: A Bot object with a reference to the appropriate
        BotModel.
        """
        path, module = os.path.split(directory)
        bot_module = None
        bot_class = None
        logger = logging.getLogger()
        bot_module = importlib.import_module(module)
        bot_class = getattr(bot_module, "Bot", None)
        if not bot_class:
            from botfriend.bot import Bot
            bot_class = Bot
            logger.debug("No Bot class defined in %s/__init__.py. Assuming the default implementation is okay.", directory)
        bot_config_file = os.path.join(directory, "bot.yaml")
        if not os.path.exists(bot_config_file):
            raise Exception(
                "Bot config file %s not found." % bot_config_file
            )
        config = yaml.safe_load(open(bot_config_file))

        # If any key is present in the default bot configuration but
        # missing here, fill in the value.
        for k, v in list(defaults.items()):
            if k == 'publish':
                # Handled separately, below.
                continue
            if not k in config:
                config[k] = v

        # Fill in missing publisher configuration if the bot has that
        # publisher enabled.
        if 'publish' in defaults:
            bot_publishers = config.get('publish')
            if bot_publishers:
                # This bot has publishers whose configuration may be incomplete.
                for publisher, default_publisher_config in list(defaults['publish'].items()):
                    publisher_config = bot_publishers.get(publisher)
                    if not publisher_config:
                        # The bot config does not use this publisher. Don't fill in its
                        # configuration, that will make it look like the bot _does_ use this
                        # publisher and the configuration is incomplete.
                        continue
                    for k, v in list(default_publisher_config.items()):
                        if not k in publisher_config:
                            publisher_config[k] = v
            
        name = config.get('name')
        if not name:
            raise Exception(
                "Bot config file (%s) does not define a value for 'name'!" %
                bot_config
            )
        bot_model, is_new = get_one_or_create(_db, BotModel, name=name)
        bot_implementation = bot_class(bot_model, directory, config)
        bot_model.implementation = bot_implementation
        return bot_model

    @property
    def should_make_new_post(self):
        """Is it time to publish a brand new post?"""
        return not self.next_post_time or self.next_post_time < _now()

    @property
    def ready_scheduled_posts(self):
        """Find all scheduled Posts that should be published now.

        :return: A list of Posts.
        
        Only Posts with no Publications are considered.

        If there are any Posts with `publish_at` before the current time,
        all such Posts are returned.

        If not, the oldest Post with `publish_at` not set is chosen.

        If there are no Posts with `publish_at` not set, an empty list
        is returned.
        """
        _db = Session.object_session(self)
        now = _now()
        base_query = _db.query(Post).filter(
            Post.bot==self).outerjoin(
                Post.publications).filter(
                    Publication.id==None)
        past_due = base_query.filter(Post.publish_at <= now).order_by(
            Post.publish_at.asc()).all()
        if past_due:
            return past_due

        if not self.should_make_new_post:
            return []
        next_in_line = base_query.filter(Post.publish_at == None).order_by(
            Post.created.asc()).limit(1).all()
        return next_in_line

    @property
    def scheduled(self):
        """All scheduled posts, in the order they will be posted.

        Posts with a specific schedule time will show up before posts
        without a schedule time.
        """
        _db = Session.object_session(self)

        base_query = _db.query(Post).outerjoin(Post.publications).filter(
            Post.bot==self).filter(
                Publication.id==None)

        # We want all scheduled posts with a specific post time to
        # show up before scheduled posts with no specific post time.
        #
        # Since SQLite doesn't support NULLS LAST, this is the simplest
        # way to do it.
        with_publish_time = base_query.filter(
            Post.publish_at != None).order_by(
                Post.publish_at.asc(), Post.id.asc()
            )
        without_publish_time = base_query.filter(
            Post.publish_at == None).order_by(Post.id.asc())
        
        return with_publish_time.all() + without_publish_time.all()
    
    def recent_posts(self, published_after=None, require_success=True):
        """Find recently published posts.

        This can be used to ensure that a bot doesn't repeat itself.

        :param published_after: Either a datetime or a number of days before
        the present.
        """
        now = _now()
        if isinstance(published_after, int):
            published_after = now - datetime.timedelta(days=published_after)
        _db = Session.object_session(self)
        qu = _db.query(Post).join(Post.publications).filter(
            Post.bot==self).filter(Publication.most_recent_attempt < now)
        if require_success:
            qu = qu.filter(Publication.error==None)
        if published_after:
            qu = qu.filter(
                Publication.most_recent_attempt > published_after).distinct(
                    Post.id
                )
        qu = qu.order_by(Publication.most_recent_attempt.desc())
        return qu

    @property
    def undeliverable_posts(self):
        """Find posts that had errrors when we tried to publish them to one or
        more publications.
        """
        _db = Session.object_session(self)
        return _db.query(Post).join(Post.publications).filter(
            Post.bot==self).filter(Publication.error != None).order_by(
                Publication.most_recent_attempt.asc()
            )                
    
    @hybrid_property
    def json_state(self):
        """Try to interpret .state as a JSON object."""
        if not self.state:
            return self.state
        return json.loads(self.state)

    @json_state.setter
    def json_state(self, state):
        self.state = json.dumps(state)

    @hybrid_property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_value):
        if not isstr(new_value):
            new_value = json.dumps(new_value)
        self._state = new_value
        self.last_state_update_time = _now()
        
    @hybrid_property
    def backlog(self):
        """Parse the bot's backlog as a JSON list."""
        if not self._backlog:
            return []
        return json.loads(self._backlog)

    @backlog.setter
    def backlog(self, backlog):
        """Set the given list as the bot's backlog.

        :param backlog: A list that can be converted into JSON.
        """
        if not isinstance(backlog, list):
            raise ValueError(
                "Backlog must be a list (got %s)" % type(backlog)
            )
        self._backlog = json.dumps(backlog)
        
    def pop_backlog(self):
        """Pop one item off the backlog.

        :return: None, if there is no backlog; otherwise, backlog
        item. Probably a string, but depending on the bot, it could be
        any JSONable item.
        """
        backlog = self.backlog
        if not backlog:
            return None
        obj = backlog[0]
        self.backlog = backlog[1:]
        return obj


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    bot_id = Column(
        Integer, ForeignKey('bots.id'), index=True, nullable=False
    )

    # The time the post was created.
    created = Column(DateTime)
    
    # The time the post was/is supposed to be published.
    publish_at = Column(DateTime)

    # The original content of the post. This may need to be cut down
    # for specific publication mechanisms, but that's okay -- we know how
    # to do that automatically.
    content = Column(Unicode)

    # A post may be marked as containing sensitive material.
    sensitive = Column(Boolean)
    
    # A Post may be a reply to another botfriend post.
    reply_to_id = Column(
        Integer, ForeignKey('posts.id'), index=True, nullable=True
    )

    # Or it might be a reply to another post on some other service.
    reply_to_foreign_id = Column(Unicode, index=True)

    # A Post may have some item of state associated with it.
    state = Column(Unicode, index=True, name="state")

    # A Post may also have some small piece of _unique_ state associated
    # with it. This is useful when a Post corresponds to a unique
    # piece of data obtained from some other source.
    external_key = Column(Unicode, index=True, unique=True, nullable=True)
    
    replies = relationship(
        "Post", backref=backref("reply_to", remote_side=[id])
    )
    
    publications = relationship('Publication', backref='post')
    attachments = relationship('Attachment', backref='post')

    def __repr__(self):
        return "<Post %s: %s>" % (self.id, self.content)

    @hybrid_property
    def json_state(self):
        """Parse the post's state as a JSON dictionary."""
        if not self.state:
            return {}
        return json.loads(self.state)

    @json_state.setter
    def json_state(self, state):
        self.state = json.dumps(state)
    
    @classmethod
    def for_external_key(cls, bot, key):
        """Find or create the Post  with the given external key.
        """
        from .bot import Bot
        if isinstance(bot, Bot):
            bot = bot.model
        _db = Session.object_session(bot)
        return get_one_or_create(_db, Post, bot=bot, external_key=key)
    
    @classmethod
    def from_content(cls, bot, content, publish_at=None, reuse_existing=True):
        """Turn a string of content into a Post.

        :param content: A string. If this is a bytestring it will be decoded as UTF-8
            before being stored.
        :param publish_at: A datetime. If provided, the post will not be published until
            this time.
        :param reuse_existing: If a Post already exists with this content,
            return it rather than creating a new one.
        """
        _db = Session.object_session(bot)
        if isinstance(content, bytes):
            content = content.decode("utf8")
        if reuse_existing:
            post, is_new = get_one_or_create(
                _db, Post, bot=bot, on_multiple='interchangeable',
                content=content
            )
        else:
            post, is_new = create(_db, Post, bot=bot)
        now = _now()
        if is_new:
            post.content = content
            post.created = now
            post.publish_at = publish_at
        return post, is_new

    @property
    def content_snippet(self):
        "A small string of content suitable for logging."
        if self.content:
            if len(self.content) > 20:
                return self.content[:20] + "…"
            return self.content
        else:
            return "[no textual content]"

    def attach(self, media_type=None, filename=None, content=None,
               alt=None):
        if not filename and not content:            
            raise ValueError(
                "Either filename or content must be provided."
            )
        if filename and content:
            raise ValueError(
                "At most one of filename and content must be provided."
            )
        if content and not media_type:
            raise ValueError(
                "Media type must be provided along with content."
            )
        _db = Session.object_session(self)
        if filename:
            # Reject a file that doesn't exist.
            if not os.path.exists(filename):
                if hasattr(self.bot.implementation, 'local_path'):
                    filename = self.bot.implementation.local_path(filename)
            if not os.path.exists(filename):
                raise ValueError(
                    "%s does not exist on disk." % filename
                )
            attachment, is_new = get_one_or_create(
                _db, Attachment, post=self, filename=filename
            )
            attachment.media_type = media_type
            attachment.alt = alt
        elif content:
            attachment = create(
                _db, Attachment, post=self, media_type=media_type,
                content=content, alt=alt
            )


class Publication(Base):
    """A record that a post was published to a specific service,
    or at least that the attempt was made.
    """
    __tablename__ = 'publications'
    id = Column(Integer, primary_key=True)
    post_id = Column(
        Integer, ForeignKey('posts.id'), index=True, nullable=False
    )

    # The service we published this post to.
    service = Column(Unicode)

    # The service uses this ID to refer to the post.
    # (e.g. Twitter assigns the post an ID when it becomes a tweet).
    external_id = Column(Unicode, index=True)
    
    # The first time we tried to publish this post.
    first_attempt = Column(DateTime)

    # The most recent time we tried to publish this post.
    most_recent_attempt = Column(DateTime)

    # The content that was posted to this service, if different from
    # the content stored in Post.content
    content = Column(Unicode)
    
    # The reason, if any, we couldn't publish this post. If this
    # is None, it is assumed the post was successfully published.
    error = Column(Unicode)

    def display(self):
        if self.error:
            msg = self.error
            if self.most_recent_attempt != self.first_attempt:
                msg += " (since %s)" % self.first_attempt
        else:
            if self.most_recent_attempt:
                msg = "Published %s" % self.most_recent_attempt.strftime(TIME_FORMAT)
            else:
                msg = "Somehow neither published nor errored."
        return "%s | %s | %s " % (self.service, msg, self.post.content_snippet)
        
    def report_attempt(self, error=None):
        "Report a (possibly successful) attempt to publish this post."
        now = _now()
        if not self.first_attempt:
            self.first_attempt = now
        self.most_recent_attempt = now
        self.error = error

    def report_success(self, external_id=None):
        self.report_attempt(error=None)
        if external_id:
            self.external_id = str(external_id)
        
    def report_failure(self, error="Unknown error."):
        if isinstance(error, Exception):
            error = str(error.message)
        self.report_attempt(error)


class Attachment(Base):
    """A file (usually a binary image) associated with a post."""
    
    __tablename__ = 'attachments'
    id = Column(Integer, primary_key=True)
    post_id = Column(
        Integer, ForeignKey('posts.id'), index=True, nullable=False
    )

    # The media type of the attachment.
    media_type = Column(Unicode)
    
    # You may store the file on disk and track it with its filename,
    # relative to the bot's directory.
    filename = Column(Unicode, index=True)
   
    # You can store the attachment directly in the database instead.
    content = Column(Binary)

    # The attachment may have alt text associated.
    alt = Column(Unicode)
