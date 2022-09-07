from django.urls import path
from . import views
from .views import (TaskListView, TaskDetailView)


urlpatterns = [
    path('', views.home, name='dashboard'),
    path('productbacklog/', TaskListView.as_view(), name='product-backlog'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('sort/', views.sort, name='sort')
]