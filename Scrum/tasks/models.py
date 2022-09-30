from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.datetime_safe import date, datetime
from django.utils.translation import gettext_lazy as _

from sprints.models import Sprint
from members.models import Member


class Task(models.Model):
    HIGH_PRIORITY = 'HI'
    MEDIUM_PRIORITY = 'ME'
    LOW_PRIORITY = 'LO'
    PRIORITY_LEVELS = [
        (HIGH_PRIORITY, 'High'),
        (MEDIUM_PRIORITY, 'Medium'),
        (LOW_PRIORITY, 'Low')
    ]

    PENDING = 'PE'
    IN_PROGRESS = 'IN'
    COMPLETE = 'CM'
    STATUS_LEVELS = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETE, 'Complete')
    ]

    EXTRA_LARGE = 'XL'
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    SHIRT_SIZES = [
        (EXTRA_LARGE, EXTRA_LARGE),
        (LARGE, LARGE),
        (MEDIUM, MEDIUM),
        (SMALL, SMALL)
    ]

    # Mandatory
    title = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_LEVELS)

    # Defaults
    status = models.CharField(max_length=20, choices=STATUS_LEVELS, default=PENDING)
    story_point = models.CharField(max_length=20, choices=SHIRT_SIZES, default=MEDIUM)

    # Optional
    tag = models.CharField(max_length=20, null=True, blank=True)
    assignee = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)

    # Developers
    date_created = models.DateTimeField(default=timezone.now)

    @property
    def days_left(self):
        today = date.today()
        days_left = self.due_date - today
        return days_left

    @property
    def get_priority_color(self):

        if self.priority == Task.HIGH_PRIORITY:
            color = 'red'
        if self.priority == Task.MEDIUM_PRIORITY:
            color = 'orange'
        if self.priority == Task.LOW_PRIORITY:
            color = 'yellow'

        return color

    def clean(self):
        if date.today() > self.due_date:
            raise ValidationError({'end_date': _('Start date needs to be present or future')})

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
