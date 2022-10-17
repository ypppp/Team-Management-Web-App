from django.urls import path

from .views import TeamAnalytics, RecentEntryView, AddEntryView

urlpatterns = [
    path('', TeamAnalytics.as_view(), name='team-anal'),
    path('entries/', RecentEntryView.as_view(), name='entry-list'),
    path('entry/new/', AddEntryView.as_view(), name='entry-create'),
]