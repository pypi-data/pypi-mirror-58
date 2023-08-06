from nose.tools import set_trace
from argparse import ArgumentParser
import logging
import os
import sys
import time

from .config import Configuration
from .model import (
    _now,
    InvalidPost,
    Post,
    TIME_FORMAT,
)


class Script(object):
    pass

class BotScript(Script):
    """A script that operates on one or more bots."""

    NAME = "Bot script"

    @property
    def log(self):
        return logging.getLogger(self.NAME)
    
    @classmethod
    def parser(cls):
        parser = ArgumentParser()
        parser.add_argument(
            '--config',
            help="Directory containing the botfriend database.",
        )
        parser.add_argument(
            'bots', 
            help='Operate on this bot.',
            metavar='BOT',
            nargs='*'
        )
        return parser
    
    def __init__(self):
        """Instantiate and run a script."""
        parser = self.parser()
        self.args = parser.parse_args()
        if self.args.config:
            config_directory = self.args.config
        else:
            config_directory = Configuration.default_directory()


        if not os.path.exists(config_directory):
            self.log.warn(
                "%s does not exist, creating it.", config_directory
            )
            os.makedirs(config_directory)

        self.log.debug("Using config directory %s", config_directory)
        self.config = Configuration.from_directory(config_directory, self.args.bots)

    @classmethod
    def run(cls):
        instance = cls()
        found = False
        for model in sorted(
                instance.config.bots,
                key=lambda x: x.implementation.module_name
        ):
            try:
                found = True
                instance.process_bot(model)
            except InvalidPost as e:
                # This _should_ crash the whole script -- we don't
                # want to commit invalid posts to the database.
                raise e
            except Exception as e:
                # Don't let a 'normal' error crash the whole script.
                model.implementation.log.error(str(e), exc_info=e)
        instance.config._db.commit()
        if not found:
            if instance.args.bots:
                instance.log.error("Could not find any bots named %s in %s.",
                                   instance.args.bots, instance.config.directory
                )
            else:
                instance.log.error("No bots in %s", instance.config.directory)
        
    def process_bot(self, bot_model):
        raise NotImplementedError()


class SingleBotScript(BotScript):
    """A script that _must_ be run against a single bot."""

    @classmethod
    def parser(cls):
        parser = ArgumentParser()
        parser.add_argument(
            '--config',
            help="Directory containing the botfriend database.",
        )
        # TODO: this should show up as 'bot' in descriptions but be
        # stored as a one-item list.
        parser.add_argument(
            'bots',
            help='Do something to one specific bot.',
            nargs=1,
        )
        return parser

class RepublicationScript(BotScript):
    """Attempt to publish already created posts that failed in their
    delivery.
    """
    @classmethod
    def parser(cls):
        parser = BotScript.parser()
        parser.add_argument(
            "--limit",
            help="Limit the number of posts to republish per bot.",
            type=int,
            default=1
        )
        return parser
    
    def process_bot(self, bot_model):
        undelivered = bot_model.undeliverable_posts.limit(self.args.limit)
        for post in undelivered:
            for publication in post.publications:
                if not publication.error:
                    continue
                # Find the publisher responsible for this
                matches  = [x for x in bot_model.implementation.publishers
                            if x.service == publication.service]
                if not matches:
                    # This bot doesn't use this publisher anymore.
                    continue
                [publisher] = matches
                bot_model.log.info(
                    "Attempting to republish to %s: %s" % (
                        publication.service,
                        post.content
                    )
                )
                bot_model.implementation.post_to_publisher(publisher, post, publication)
                if publication.error:
                    bot_model.log.info("Failure: %s" % publication.error)
                else:
                    bot_model.log.info("Success!")


class BotListScript(BotScript):
    """List your bots."""

    def process_bot(self, model):
        print(model.implementation.module_name)


class DashboardScript(BotScript):
    """Display the current status of one or more bots."""
    def process_bot(self, bot_model):

        now = _now()
        recent = bot_model.recent_posts().limit(1).all()
        if not recent:
            bot_model.log.info("Has never posted.")
        else:
            [recent] = recent
            bot_model.log.info("Most recent post: %s" % recent.content)
            for publication in recent.publications:
                if publication.error:
                    bot_model.log.info(
                        "%s ERROR: %s" % (publication.service, publication.error)
                    )
                else:
                    bot_model.log.info(
                        "%s posted %dm ago (%s)" % (
                            publication.service,
                            (now-publication.most_recent_attempt).total_seconds()/60,
                            publication.most_recent_attempt,
                        )
                    )

        def announce_list(count, content, what):
            if count == 1:
                item = "post"
            else:
                item = "posts"
            bot_model.log.info("%d %s %s" % (count, item, what))
            bot_model.log.info("Next up: %s" % content)
                    
        # Announce scheduled posts.
        scheduled = bot_model.scheduled
        next_post_time = bot_model.next_post_time
        if len(scheduled) > 0:
            first = scheduled[0]
            announce_list(len(scheduled), first.content, "scheduled")
            next_post_time = first.publish_at or bot_model.next_post_time

        # Announce backlog posts.
        try:
            backlog = bot_model.backlog
            if backlog:
                first = backlog[0]
                announce_list(len(backlog), first, "in backlog")
        except ValueError as e:
            pass
        
        if next_post_time:
            minutes = (next_post_time-now).total_seconds()/60
            if minutes < 0:
                when = "ASAP"
            else:
                when = "in %dm" % minutes
            bot_model.log.info("Next post %s" % when)
        else:
            bot_model.log.info("Next post not scheduled.")

            
class PostScript(BotScript):
    """Create a new post for one or all bots."""

    @classmethod
    def parser(cls):
        parser = BotScript.parser()
        parser.add_argument(
            '--dry-run',
            help="Show what would be posted, but don't post it or commit to the database.",
            action='store_true'
        )
        parser.add_argument(
            '--force',
            help="Post even if the scheduler would not normally post now.",
            action='store_true'
        )
        return parser
    
    def process_bot(self, bot_model):
        implementation = bot_model.implementation
        if self.args.force:
            bot_model.next_post_time = _now()
        posts = implementation.publishable_posts
        if self.args.dry_run:
            print(bot_model.name)
            for post in posts:
                print(post.content)
                print("-" * 80)
                return

        # We're doing this for real.
        for post in posts:
            for publication in implementation.publish(post):
                publication.post.bot.log.info(publication.display())
        self.config._db.commit()

class StateAwareScript(BotScript):

    def _state_status(self, bot_model):
        """Create a string describing the bot's current stored state."""
        if bot_model.state:
            prefix = "State"
            suffix = ":"
            state = "\n%s" % bot_model.state
        else:
            prefix = "No state"
            suffix = "."
            state = ""
        update = bot_model.last_state_update_time
        if update:
            last_update = "(last state update %s)" % update
        else:
            last_update = "(state was never updated)"
        return "%s for %s %s%s%s" % (
            prefix, bot_model.name, last_update, suffix, state
        )
        

class StateShowScript(StateAwareScript):
    """Show the internal state for a bot."""

    def process_bot(self, bot_model):
        last_update = bot_model.last_state_update_time
        print(self._state_status(bot_model))

class StateSetScript(StateAwareScript):
    """Set the internal state for a bot."""

    @classmethod
    def parser(cls):
        parser = SingleBotScript.parser()
        parser.add_argument(
            "--file",
            help="Load from this file instead of standard input.",
            default=None
        )
        return parser
    
    def process_bot(self, bot_model):
        if self.args.file:
            fh = open(self.args.file)
        else:
            fh = sys.stdin
        data = fh.read()
        if isinstance(data, bytes):
            data = data.decode("utf8")
        bot_model.state = data
        print(bot_model.state)


class StateClearScript(StateAwareScript):
    """Clear the internal state for a bot."""
   
    def process_bot(self, bot_model):
        bot_model.state = None
        bot_model.last_state_update_time = None


class StateRefreshScript(StateAwareScript):
    """Refresh the internal state for a bot."""

    def process_bot(self, bot_model):
        bot_model.implementation.check_and_update_state(force=True)
        print(self._state_status(bot_model))

class StressTestScript(BotScript):
    """Stress-test a bot's generative capabilities without posting anything."""

    @classmethod
    def parser(cls):
        parser = BotScript.parser()
        parser.add_argument(
            '--rounds',
            help="Run the bot's generator this many times. (Default is 10,000)",
            type=int,
            default=10000
        )
        return parser

    def process_bot(self, bot_model):
        bot_model.implementation.stress_test(self.args.rounds)

class PublisherTestScript(BotScript):
    """Verify  that a bot's publishers are functioning without posting anything."""

    def process_bot(self, bot_model):
        for publisher in bot_model.implementation.publishers:
            try:
                result = publisher.self_test() or ""
                print("GOOD %s %s %s" % (bot_model.name, publisher.service, result))
            except Exception as e:
                print("FAIL %s %s: %s" % (
                    bot_model.name, publisher.service, e
                ))        

class BacklogShowScript(BotScript):
    """Show the backlog posts for a bot."""

    @classmethod
    def parser(cls):
        parser = BotScript.parser()
        parser.add_argument(
            "--limit",
            help="Limit the number of backlog posts shown.",
            type=int,
            default=None
        )
        return parser

    def process_bot(self, bot_model):
        backlog = bot_model.implementation.backlog
        count = len(backlog)
        if self.args.limit:
            max_i = self.args.limit - 1
        else:
            max_i = None
        if count:
            if count == 1:
                item = "post"
            else:
                item = "posts"
            bot_model.log.info("%d %s in backlog" % (count, item))
            for i, content in enumerate(backlog):
                bot_model.log.info(content)
                if max_i is not None and i > max_i:
                    break
        else:
            bot_model.log.info("No backlog.")

class BacklogLoadScript(SingleBotScript):

    NAME = "Backlog load script"
    
    @classmethod
    def parser(cls):
        parser = SingleBotScript.parser()
        parser.add_argument(
            "--file",
            help="Load from this file instead of standard input.",
            default=None
        )
        return parser
    
    def process_bot(self, bot_model):
        if self.args.file:
            fh = open(self.args.file)
        else:
            fh = sys.stdin
        bot = bot_model.implementation
        # Process one backlog item per line of the input file.
        items = []
        for line in fh.readlines():
            line = line.strip()
            if isinstance(line, bytes):
                line = line.decode("utf8")
            try:
                items.append(bot.prepare_input(line))
            except InvalidPost as e:
                self.log.error(
                    "Could not import %s: %s", line, str(e)
                )
        bot.extend_backlog(items)
        self.log.info("Appended %d items to backlog." % len(items))
        self.log.info("Backlog size now %d items" % len(bot_model.backlog))


class BacklogClearScript(SingleBotScript):

    def process_bot(self, bot_model):
        backlog = bot_model.backlog
        if backlog:
            bot_model.log.warn(
                "About to clear the backlog for %s.", bot_model.name
            )
            bot_model.log.warn(
                "Sleeping for 2 seconds to give you a chance to Ctrl-C."
            )
            time.sleep(2)
            bot_model.implementation.clear_backlog()
                
class ScheduledPostsShowScript(BotScript):
    """Show the scheduled posts for a bot."""

    @classmethod
    def parser(cls):
        parser = BotScript.parser()
        parser.add_argument(
            "--limit",
            help="Limit the number of scheduled posts shown.",
            type=int,
            default=None
        )
        return parser

    def process_bot(self, bot_model):
        scheduled = bot_model.scheduled
        count = len(scheduled)
        if self.args.limit:
            max_i = self.args.limit - 1
        else:
            max_i = None
        if count:
            if count == 1:
                item = "post"
            else:
                item = "posts"
            bot_model.log.info("%d scheduled %s" % (count, item))
            for i, post in enumerate(scheduled):
                if max_i is not None and i > max_i:
                    break
                if post.publish_at:
                    when_post = post.publish_at.strftime(TIME_FORMAT)
                elif i == 0 and bot_model.next_post_time:
                    when_post = bot_model.next_post_time.strftime(TIME_FORMAT)
                else:
                    when_post = "No scheduled time"
                bot_model.log.info("%s | %s" % (when_post, post.content))
        else:
            bot_model.log.info("No scheduled posts.")


class ScheduledPostsLoadScript(SingleBotScript):

    @classmethod
    def parser(cls):
        parser = SingleBotScript.parser()
        parser.add_argument(
            "--file",
            help="Load scheduled posts from this file.",
            default=None
        )
        return parser
    
    def process_bot(self, bot_model):
        if self.args.file:
            fh = open(self.args.file)
        else:
            fh = None
        bot_model.implementation.schedule_posts(fh)


class ScheduledPostsClearScript(SingleBotScript):

    def process_bot(self, bot_model):
        scheduled = list(bot_model.scheduled)
        if scheduled:
            bot_model.log.warn(
                "About to remove all scheduled posts for %s.", bot_model.name
            )
            bot_model.log.warn(
                "Sleeping for 2 seconds to give you a chance to Ctrl-C."
            )
            time.sleep(2)
            _db = self.config._db
            for post in scheduled:
                for publication in post.publications:
                    _db.delete(publication)
                for attachment in post.attachments:
                    _db.delete(attachment)
                _db.delete(post)

        # Also reset the next post time.
        bot_model.next_post_time = bot_model.implementation.schedule_next_post([])
        if bot_model.next_post_time:
            bot_model.log.info("Next post at %s", bot_model.next_post_time)
        else:
            bot_model.log.info("Ready to post.")
