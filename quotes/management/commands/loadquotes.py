from django.core.management.base import BaseCommand, CommandError
from quotes.models import Tag, Quote
import json


class Command(BaseCommand):
    help = "Upload quotes from json to db"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs=1)

    def handle(self, *args, **options):
        path = options['path'][0]
        try:
            with open(path) as file:
                data = json.load(file)
                for quote_data in data:
                    quote = Quote(quote=quote_data['quote'])
        except FileNotFoundError:
            raise CommandError('File "%s" not found' % path)
