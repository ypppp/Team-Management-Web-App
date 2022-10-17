from django.urls import path

from .views import MemberListView, MemberDetailView, MemberCreateView, MemberUpdateView

urlpatterns = [
    path('', MemberListView.as_view(), name='member-list'),
    path('member/new/', MemberCreateView.as_view(), name='member-create'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('member/<int:pk>/update/', MemberUpdateView.as_view(), name='member-update'),
]