from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import date
from django.utils.translation import gettext_lazy as _


class Sprint(models.Model):

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
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    # Developers
    date_created = models.DateTimeField(default=timezone.now)
    sprint_complete = models.BooleanField(default=False)

    def clean(self):
        if date.today() > self.start_date:
            raise ValidationError({'end_date':_('Start date needs to be present or future')})

        if date.today() > self.end_date:
            raise ValidationError({'end_date':_('End date needs to be present or future')})

        if self.start_date > self.end_date:
            raise ValidationError({'end_date:':_('End date must be set on or before start date')})

    @property
    def duration(self):
        return self.end_date - self.start_date

    @property
    def days_left(self):
        today = date.today()
        days_left = self.end_date - today
        return days_left

    def __str__(self):
        return self.title