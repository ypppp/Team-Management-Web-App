from django import forms

from sprints.models import Sprint
from tasks.models import Task


class SprintForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Must not contain spaces'})
    )

    sprint_goal = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Tell us more about this sprint',
                                     'rows': '3', })
    )

    end_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d',
                               attrs={'class': 'form-control',
                                      'placeholder': 'Select end date',
                                      'type': 'date'
                                      })
    )

    start_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d',
                               attrs={'class': 'form-control',
                                      'placeholder': 'Select end date',
                                      'type': 'date'
                                      })
    )

    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.filter(sprint=None), required=False)

    class Meta:
        model = Sprint
        fields = [
            'title',
            'sprint_goal',
            'start_date',
            'end_date',
            'tasks',
        ]
