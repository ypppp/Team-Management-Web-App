import json
from datetime import datetime

from django.core.management.base import BaseCommand

from sprints.models import Sprint


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('sprints.json') as f:
            sprints_json = json.load(f)

        for sprint in sprints_json['objects']:

            start_date = sprint['start_date'][:10]
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            sprint['start_date'] = start_date

            end_date = sprint['end_date'][:10]
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            sprint['end_date'] = end_date

            new_sprint = Sprint(title=sprint['title'],
                                sprint_goal=sprint['sprint_goal'],
                                start_date=sprint['start_date'],
                                end_date=sprint['end_date'])
            new_sprint.save()
