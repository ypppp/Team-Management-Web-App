from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta


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
    # end_date = models.DateTimeField(null=True, blank=True, validators=[validate_start_end_datetime])
    end_date = models.DateTimeField(null=True, blank=True)

    # Developers
    date_created = models.DateTimeField(default=timezone.now)  # auto_now_add=False)
    sprint_complete = models.BooleanField(default=False)

    def validate_start_end_datetime(self):
        if self.start_date > self.end_date:
            raise ValidationError(
                '%(start)s must not be larger than (end)s',
                params={'start': self.start_date, 'end': self.end_date},
            )
