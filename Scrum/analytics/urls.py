from django.urls import path

from .views import DailyTeamAnalytics, RecentEntryView, AddEntryView

urlpatterns = [
    path('daily/', DailyTeamAnalytics.as_view(), name='team-stat'),
    path('entries/', RecentEntryView.as_view(), name='entry-list'),
    path('entry/new/', AddEntryView.as_view(), name='entry-create'),
]