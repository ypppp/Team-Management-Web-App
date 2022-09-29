from django import forms
from .models import Sprint


class SprintForm(forms.ModelForm):
    sprint_Name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Give your sprint a title'}
    ), error_messages={'required': 'Sprint name cannot contain invalid characters'})

    sprint_Goal = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Give your sprint a goal', 'rows': 4}
    ))

    class Meta:
        model = Sprint
        fields = ['sprint_Name',
                  'sprint_Goal',
                  'task',
                  'assignee',
                  'duration',
                  'start_Date',
                  'end_Date',
                  'created_Date',
                  'is_Sprint_Complete']

        widgets = {
            'start_Date': forms.DateTimeInput(
                format='%d-%m-%Y',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'end_Date': forms.DateTimeInput(
                format='%d-%m-%Y',
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),

        }