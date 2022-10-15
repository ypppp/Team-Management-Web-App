from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from tasks.models import Task


class EntryForm(forms.ModelForm):
    task = forms.ModelChoiceField(queryset=Task.objects.all())
    date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d',
                               attrs={'class': 'form-control',
                                      'placeholder': 'Select a date',
                                      'type': 'date'}))
    duration = forms.DurationField()

    def clean(self):
        if timedelta(hours=24) < self.duration:
            raise ValidationError({'duration': _('That hardworking?')})