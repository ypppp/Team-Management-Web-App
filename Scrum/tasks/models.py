from django.db import models
from django.urls import reverse
from django.utils import timezone
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

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})

    @property
    def get_priority_color(self):

        if self.priority == Task.HIGH_PRIORITY:
            color = 'red'
        if self.priority == Task.MEDIUM_PRIORITY:
            color = 'orange'
        if self.priority == Task.LOW_PRIORITY:
            color = 'yellow'

        return color

    def __str__(self):
        return self.title
