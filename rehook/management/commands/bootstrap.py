from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username='tom').exists():
            User.objects.create_superuser('tom', 'tom.punihaole@gmail.com', 'test123')
