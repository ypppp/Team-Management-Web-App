from django.urls import path
from .views import (SprintListView, SprintDetailView, SprintCreateView,
                    SprintUpdateView, SprintDeleteView, toggle_start_end)


urlpatterns = [
    path('', SprintListView.as_view(), name='sprint-list'),
    path('sprint/new/', SprintCreateView.as_view(), name='sprint-create'),
    path('sprint/<int:pk>/', SprintDetailView.as_view(), name='sprint-detail'),
    path('sprint/<int:pk>/update/', SprintUpdateView.as_view(), name='sprint-update'),
    path('sprint/<int:pk>/delete/', SprintDeleteView.as_view(), name='sprint-delete'),
    path('sprint/<int:pk>/start_end/', toggle_start_end, name='start-end'),
]

