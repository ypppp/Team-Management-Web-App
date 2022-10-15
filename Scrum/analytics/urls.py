from django.urls import path

from .views import TeamAnalytics, RecentEntryView

urlpatterns = [
    # path('', TeamStat.as_view(), name='team-stat'),
    path('<int:pk>/', TeamAnalytics.as_view(), name='team-stat'),
    path('entries/', RecentEntryView.as_view(), name='entry-list'),
]