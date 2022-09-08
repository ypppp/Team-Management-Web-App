from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'user_story',
            'assignee',
            'status',
            'priority',
            'tag',
            'sprint',
            'due_date',
        ]