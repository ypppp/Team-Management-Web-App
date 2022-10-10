import json
from datetime import datetime

from django.core.management.base import BaseCommand

from tasks.models import Task


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('tasks.json') as f:
            tasks_json = json.load(f)

        for task in tasks_json['objects']:

            due_date = task['due_date'][:10]
            due_date = datetime.strptime(due_date, '%Y-%m-%d')
            task['due_date'] = due_date

            if 'XX' in task['story_point']:
                task['story_point'] = task['story_point'][-2:]

            new_task = Task(title=task['title'], description=task['description'],
                            due_date=task['due_date'], tag=task['tag'],
                            story_point=task['story_point'])
            new_task.save()
