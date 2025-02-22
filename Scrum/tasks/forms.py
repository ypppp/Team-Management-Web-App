from django import forms

from members.models import Member
from sprints.models import Sprint
from .models import Task


class TaskForm(forms.ModelForm):
    # Mandatory
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Give your task a meaningful title', })
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Add more details to this task',
                                     'rows': '3', })
    )

    priority = forms.ChoiceField(choices=Task.PRIORITY_LEVELS)

    # Defaults
    status = forms.ChoiceField(choices=Task.STATUS_LEVELS, required=False)
    story_point = forms.ChoiceField(choices=Task.SHIRT_SIZES, required=False)

    # Optional
    tag = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Tag a topic', }),
        required=False
    )

    assignee = forms.ModelChoiceField(
        queryset=Member.objects.all(), empty_label='---unassigned---', required=False)

    sprint = forms.ModelChoiceField(
        queryset=Sprint.objects.filter(status=Sprint.PENDING),
        empty_label='---unallocated---', required=False)

    due_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d',
                               attrs={'class': 'form-control',
                                      'placeholder': 'Select a date',
                                      'type': 'date'}))

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'priority',
            'status',
            'story_point',
            'tag',
            'assignee',
            'sprint',
            'due_date',
        ]

