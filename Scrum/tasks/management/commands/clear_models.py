from django.core.management.base import BaseCommand
from Scrum.tasks.models import Task


class Command(BaseCommand):
    def handle(self, *args, **options):
        Task.objects.all().delete()


