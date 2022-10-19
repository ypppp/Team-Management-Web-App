from django.contrib import admin
from .models import Task


admin.site.register(Task)

class TaskInline(admin.TabularInline):
    model = Task

class SprintAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]