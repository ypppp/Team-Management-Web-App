from django.urls import path

from .views import MemberListView, MemberCreateView

urlpatterns = [
    path('', MemberListView.as_view(), name='member-list'),
    path('member/new/', MemberCreateView.as_view(), name='member-create')
]
