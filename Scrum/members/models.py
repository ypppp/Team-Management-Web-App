from datetime import timedelta
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Member(models.Model):
    # Mandatory
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    # Optional
    nickname = models.CharField(max_length=20, default='')
    cumulative_work = models.DurationField(default=timedelta(0))

    # Developers
    date_created = models.DateTimeField(default=timezone.now, editable=False)

    def get_absolute_url(self):
        return reverse('member-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


