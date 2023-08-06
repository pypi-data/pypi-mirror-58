import logging

from cliff.lister import Lister
from tracklr import Tracklr


class Ls(Lister):

    log = logging.getLogger(__name__)

    tracklr = Tracklr()

    def take_action(self, parsed_args):
        """Generates report and logs total number of hours."""
        ts = self.tracklr.get_report(
            parsed_args.kalendar,
            parsed_args.date,
            parsed_args.include,
            parsed_args.exclude,
        )

        titles = self.tracklr.get_titles(
            parsed_args.kalendar, parsed_args.title, parsed_args.subtitle
        )
        self.log.info(titles)
        self.log.info("Total hours: {}".format(self.tracklr.total_hours))
        self.log.info("Number of events: {}".format(len(ts)))

        return (("Date", "Summary", "Description", "Hours"), ts)

    def get_description(self):
        """Returns command description"""
        return "creates report"

    def get_parser(self, prog_name):
        """Gets default parser ie. this command does not add any new args"""
        parser = super(Ls, self).get_parser(prog_name)
        return self.tracklr.get_parser(parser)
