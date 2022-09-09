from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Give your task a title', }
    ), label='')

    assignee = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Assign a member', }
    ), required=False)

    tag = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Tag a topic', }
    ), required=False)

    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Add more details to this task',
               'rows': '5', }
    ))

    user_story = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'As a ... I want to ...',
               'rows': '2'}
    ), required=False)

    class Meta:
        model = Task
        fields = [
            'title',
            'assignee',
            'due_date',
            'status',
            'priority',
            'tag',
            'sprint',
            'description',
            'user_story',
        ]

        widgets = {
            'due_date': forms.DateTimeInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),

        }

