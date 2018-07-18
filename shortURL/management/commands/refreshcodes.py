from django.core.management import BaseCommand, CommandError
from shortURL.models import Link


class Command(BaseCommand):
    help = 'Refreshes shortcodes of entries in the database'

    def handle(self, *args, **options):
        return Link.objects.refresh_code()