from django import forms

from sprints.models import Sprint
from tasks.models import Task


class SprintForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'A meaningful title'})
    )

    sprint_goal = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Add more details to this task',
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

    task = forms.ModelChoiceField(
        queryset=Task.objects.all(), empty_label='Unallocated', required=False)

    class Meta:
        model = Sprint
        fields = [
            'title',
            'sprint_goal',
            'start_date',
            'end_date',
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if ' ' in title:
            raise forms.ValidationError('Space not allowed')
        return title

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')

        if start_date > end_date:
            raise forms.ValidationError('End date must be after start date')
        return end_date