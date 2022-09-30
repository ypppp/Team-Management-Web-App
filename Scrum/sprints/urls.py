from django.urls import path
from sprints.views import SprintListView

urlpatterns = [
    path('sprintlist/', SprintListView.as_view(), name='sprint-list'),
    #path('sprint/<int:pk>/', SprintDetailView.as_view(), name='sprint-detail'),

]