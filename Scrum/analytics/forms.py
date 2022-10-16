from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Sum

from analytics.models import Entry
from sprints.models import Sprint
from tasks.models import Task


class EntryForm(forms.ModelForm):
    # Mandatory
    task = forms.ModelChoiceField(queryset=None, empty_label='Choose a task')
    date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d',
                               attrs={'type': 'date'}))
    duration = forms.IntegerField(max_value=24, min_value=1, label='Worked Hours')

    class Meta:
        model = Entry
        exclude = [
            'timestamp',
        ]

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)

        sprint = Sprint.objects.filter(status=Sprint.ONGOING).first()

        self.fields['task'].queryset = Task.objects.filter(sprint=sprint)

        self.fields['date'].widget.attrs.update({'min': sprint.start_date,
                                                 'max': sprint.end_date})

    def clean_duration(self):
        duration = self.cleaned_data['duration']
        date = self.cleaned_data['date']

        # int to timedelta
        print(duration)
        duration = timedelta(hours=duration)

        # input > 24 hours
        if timedelta(hours=24) < duration:
            raise ValidationError('That hardworking?')

        entries = Entry.objects.filter(date=date)
        if entries.count() > 0:
            agg = entries.aggregate(total=Sum('duration'))
            print(entries, agg)

            # already 24 hours
            if agg['total'] >= timedelta(hours=24):
                raise ValidationError('You have worked 24 hours for the day')

            # overflow cap
            if agg['total'] + duration > timedelta(hours=24):
                overflow = agg['total'] + duration - timedelta(hours=24)
                print(overflow)
                duration -= overflow

        return duration