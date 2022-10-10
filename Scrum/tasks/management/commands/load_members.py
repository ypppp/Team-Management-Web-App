from django.core.management.base import BaseCommand
import json
from members.models import Member


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('members.json') as f:
            members_json = json.load(f)

        for member in members_json['objects']:
            new_member = Member(first_name=member['first_name'],
                                last_name=member['last_name'],
                                email=member['email'])
            new_member.save()
