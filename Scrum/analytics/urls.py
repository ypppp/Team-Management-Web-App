from django.urls import path

from .views import DailyTeamAnalytics, RecentEntryView, AddEntryView

urlpatterns = [
    path('', DailyTeamAnalytics.as_view(), name='team-anal'),
    path('entries/', RecentEntryView.as_view(), name='entry-list'),
    path('entry/new/', AddEntryView.as_view(), name='entry-create'),
]