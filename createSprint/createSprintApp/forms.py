from django import forms
from .models import Sprint


class SprintForm(forms.ModelForm):
    sprint_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Give your sprint a title'}
    ))

    sprint_goal = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Give your sprint a goal', 'rows': 4}
    ))

    class Meta:
        model = Sprint
        fields = ['sprint_name',
                  'sprint_goal',
                  'task',
                  'assignee',
                  'duration',
                  'start_date',
                  'end_date',
                  'created_date',
                  'is_sprint_complete']

        widgets = {
            'start_date': forms.DateTimeInput(
                format='%d-%m-%Y',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'end_date': forms.DateTimeInput(
                format='%d-%m-%Y',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),

        }