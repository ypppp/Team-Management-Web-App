from datetime import timedelta
from django.db import models


class Member(models.Model):

    # Mandatory
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    # Optional
    cumulative_work = models.DurationField(default=timedelta(0))
