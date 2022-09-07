from django import forms
from .models import Task


class TaskForm(forms):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'assignee',
            'status',
            'priority',
            'tag',
            'sprint',
            'due_date'
        ]
