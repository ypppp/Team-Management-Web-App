from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from analytics.models import Entry
from sprints.models import Sprint
from tasks.models import Task


class EntryForm(forms.ModelForm):
    task = forms.ModelChoiceField(queryset=Task.objects.all())
    date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d',
                               attrs={'type': 'date',
                                      # 'min': '',
                                      }
                               )
    )
    duration = forms.DurationField()

    class Meta:
        model = Entry
        exclude = [
            'timestamp',
        ]

    # def __init__(self, *args, **kwargs):
    #     super(EntryForm, self).__init__(*args, **kwargs)
    #     sprint = Sprint.objects.filter(status=Sprint.ONGOING)
    #     self.fields['task'].queryset = Task.objects.filter(sprint=sprint)

    def clean(self):
        if timedelta(hours=24) < self.cleaned_data['duration']:
            raise ValidationError({'duration': _('That hardworking?')})