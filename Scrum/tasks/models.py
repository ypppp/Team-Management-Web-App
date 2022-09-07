from django.db import models
from django.utils import timezone

class Task(models.Model):

    PRIORITY_LEVELS = [
        ('HI', 'High'),
        ('ME', 'Medium'),
        ('LO', 'Low')
    ]

    STATUS_LEVELS = [
        ('PE', 'Pending'),
        ('IN', 'In Progress'),
        ('CM', 'Complete')
    ]

    title = models.CharField(max_length=100)

    priority = models.CharField(blank=True,
                                choices=PRIORITY_LEVELS,
                                max_length=20)

    status = models.CharField(blank=True,
                              choices=STATUS_LEVELS,
                              max_length=20)

    tag = models.CharField(max_length=50)
    assignee = models.CharField(max_length=50)
    description = models.TextField()
    user_story = models.TextField()
    sprint = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()


