from django.urls import path
from sprints.views import SprintDetailView, toggle_start, SprintListView

urlpatterns = [
    path('sprint/<int:pk>/', SprintDetailView.as_view(), name='sprint-detail'),
    path('start/<int:id>', toggle_start, name='start'),
    path('sprintlist/', SprintListView.as_view(), name='sprint-list'),
]

