from django.urls import path
from . import views
from .views import (TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView)
from .forms import TaskForm


urlpatterns = [
    path('', views.home, name='dashboard'),
    path('productbacklog/', TaskListView.as_view(), name='product-backlog'),
    path('task/<int:pk>/', TaskUpdateView.as_view(), name='task-form'),
    # path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', TaskCreateView.as_view(), name='task-create')
]