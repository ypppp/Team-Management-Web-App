from django import forms
from django.utils.datetime_safe import date
from members.models import Member
from sprints.models import Sprint
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TaskForm(forms.ModelForm):

    # Mandatory
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Give your task a title', })
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
        queryset=Member.objects.all(), empty_label='Unassigned', required=False)

    sprint = forms.ModelChoiceField(
        queryset=Sprint.objects.all(), empty_label='Unallocated', required=False)

    due_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d',
                               attrs={'class': 'form-control',
                                      'placeholder': 'Select a date',
                                      'type': 'date'}))

    # def __init__(self, *args, **kwargs):
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #
    #     # Add 'Submit' & 'Cancel' button
    #     self.helper.add_input(Submit('submit', 'Submit',
    #                                  css_class='btn-success'))
    #     self.helper.add_input(Submit('cancel', 'Cancel',
    #                                  css_class='btn-danger',
    #                                  formnovalidate='formnovalidate'))

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

        # widgets = {
        #     'due_date': forms.DateTimeInput(
        #         format='%Y-%m-%d',
        #         attrs={'class': 'form-control',
        #                'placeholder': 'Select a date',
        #                'type': 'date'
        #                }),
        #
        # }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date < date.today():
            raise forms.ValidationError('Due date must be present or future')
        return due_date
