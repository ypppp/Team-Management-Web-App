from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import date


class Entry(models.Model):
    # Mandatory
    task = models.ForeignKey(to='tasks.Task',
                             on_delete=models.CASCADE,
                             related_name='entries',)

    date = models.DateField(default=date.today)

    duration = models.DurationField()

    # Developers
    timestamp = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name_plural = 'entries'
