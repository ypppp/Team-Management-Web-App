from django.urls import path
from .views import (SprintListView, SprintDetailView, SprintCreateView,
                    SprintUpdateView, SprintDeleteView, toggle_start_end)


urlpatterns = [
    path('sprintbacklog/', SprintListView.as_view(), name='sprint-backlog'),
    path('sprint/<int:pk>/', SprintDetailView.as_view(), name='sprint-detail'),
    path('start_end/<int:id>/', toggle_start_end, name='start-end'),
    path('sprint/new/', SprintCreateView.as_view(), name='sprint-create'),
    path('sprint/<int:pk>/update/', SprintUpdateView.as_view(), name='sprint-update'),
    path('sprint/<int:pk>/delete/', SprintDeleteView.as_view(), name='sprint-delete'),
]

