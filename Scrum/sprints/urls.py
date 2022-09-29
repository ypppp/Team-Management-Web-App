from django.urls import path
from sprints.views import SprintListView

urlpatterns = [
    path('sprint/', SprintListView.as_view(), name='sprint-board')
]
