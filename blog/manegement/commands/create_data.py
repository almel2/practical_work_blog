from django.core.management import BaseCommand
from faker import Faker
from blog.models import Post, Comment


class Command(BaseCommand):
    help = 'This command create data, has one argument "count_data"'

    def add_arguments(self, parser):
        parser.add_argument('count_data', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        num = options['count_data']