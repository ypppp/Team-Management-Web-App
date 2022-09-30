from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Sprint(models.Model):

    ONE_WEEK = timedelta(weeks=1)
    TWO_WEEKS = timedelta(weeks=2)
    THREE_WEEKS = timedelta(weeks=3)
    FOUR_WEEKS = timedelta(weeks=4)

    DURATION_LEVELS = [
        (ONE_WEEK, '1 Week'),
        (TWO_WEEKS, '2 Weeks'),
        (THREE_WEEKS, '3 Weeks'),
        (FOUR_WEEKS, '4 Weeks')
    ]

    PENDING = 'PE'
    ONGOING = 'IN'
    ENDED = 'CM'

    STATUS_LEVELS = [
        (PENDING, 'Pending'),
        (ONGOING, 'Ongoing'),
        (ENDED, 'Ended')
    ]

    # Mandatory
    title = models.CharField(max_length=50, unique=True)
    sprint_goal = models.TextField()

    # Defaults
    status = models.CharField(max_length=20, choices=STATUS_LEVELS, default=PENDING)

    # Optional
    duration = models.DurationField(choices=DURATION_LEVELS, null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    # Developers
    date_created = models.DateTimeField(default=timezone.now)  # auto_now_add=False)
    sprint_complete = models.BooleanField(default=False)

    def clean(self):
        if datetime.now() > self.start_date:
            raise ValidationError({'end_date':_('Start date needs to be present or future')})

        if datetime.now() > self.end_date:
            raise ValidationError({'end_date':_('End date needs to be present or future')})

        if self.start_date > self.end_date:
            raise ValidationError({'end_date:':_('End date must be set on or before start date')})

    def __str__(self):
        return self.title