from django import forms
from django.db.models import Q
from django.utils.datetime_safe import date

from sprints.models import Sprint
from tasks.models import Task


class SprintForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Must not contain spaces',
                                      }))

    sprint_goal = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Tell us more about this sprint',
                                     'rows': '3',
                                     }))

    end_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d',
                               attrs={'class': 'form-control',
                                      'min': date.today(),
                                      'type': 'date'
                                      }))

    start_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d',
                               attrs={'class': 'form-control',
                                      'min': date.today(),
                                      'type': 'date'
                                      }))

    tasks = forms.ModelMultipleChoiceField(
        label='', queryset=Task.objects.filter(sprint=None),
        widget=forms.CheckboxSelectMultiple(), required=False)

    class Meta:
        model = Sprint
        fields = [
            'title',
            'sprint_goal',
            'start_date',
            'end_date',
            'tasks',
        ]

    def __init__(self, *args, **kwargs):
        super(SprintForm, self).__init__(*args, **kwargs)
        if self.instance.pk is not None:
            self.fields['tasks'].queryset = Task.objects.filter(Q(sprint=self.instance) | Q(sprint=None))
            tasks = self.instance.tasks.all
            self.initial['tasks'] = tasks

    def save(self, commit=True):
        sprint = super().save(commit)
        sprint.tasks.set(self.cleaned_data['tasks'])
        return sprint
