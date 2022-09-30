from django.core.management.base import BaseCommand
from tasks.models import Task
from sprints.models import Sprint


class Command(BaseCommand):

    def handle(self, *args, **options):
        Task.objects.all().delete()
        Sprint.objects.all().delete()

