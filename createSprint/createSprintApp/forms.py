from django import forms
from .models import Sprint


class SprintForm(forms.ModelForm):
    sprint_goal = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Give your sprint a goal', 'size': 100}
    ))

    class Meta:
        model = Sprint
        fields = ['sprint_goal',
                  'task',
                  'assignee',
                  'duration',
                  'start_date',
                  'end_date',
                  'created_date']

        widgets = {
            'start_date': forms.DateTimeInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'end_date': forms.DateTimeInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),

        }
