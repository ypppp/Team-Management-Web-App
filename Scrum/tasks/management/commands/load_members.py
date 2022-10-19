import json

from django.core.management.base import BaseCommand
from django.db import transaction

from members.models import Member


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('members.json') as f:
            members_json = json.load(f)

        with transaction.atomic():
            for member in members_json['objects']:
                new_member = Member(first_name=member['first_name'],
                                    last_name=member['last_name'],
                                    email=member['email'],
                                    nickname=member['genre'] + member['color_hex'][:5],
                                    )
                new_member.save()
