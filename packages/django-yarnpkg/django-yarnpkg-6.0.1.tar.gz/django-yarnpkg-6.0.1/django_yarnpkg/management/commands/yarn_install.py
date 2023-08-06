from optparse import make_option
from ..base import BaseYarnCommand


class Command(BaseYarnCommand):
    help = 'Install yarn apps'

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        self._install(args)
