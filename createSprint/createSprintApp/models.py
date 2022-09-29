from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import date


class Sprint(models.Model):
    DURATION_LEVELS = [
        ('1W', '1 Week'),
        ('2W', '2 Weeks'),
        ('3W', '3 Weeks'),
        ('4W', '4 Weeks')
    ]

    TASKS = [
        ('T1', 'Task 1'),
        ('T2', 'Task 2'),
        ('T3', 'Task 3'),
        ('T4', 'Task 4')
    ]

    sprint_goal = models.CharField(max_length=250, default="")
    task = models.CharField(blank=True, choices=TASKS, max_length=20)
    assignee = models.CharField(max_length=100, default="")
    duration = models.CharField(blank=True, choices=DURATION_LEVELS, max_length=10)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, auto_now_add=False)

