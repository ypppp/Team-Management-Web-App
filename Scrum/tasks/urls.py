from django.urls import path
from tasks.views import (TaskListView, TaskDetailView, TaskCreateView, TaskDeleteView,
                         TaskListViewSortBySprintAscending, TaskListViewSortByAssigneeAscending,
                         TaskListViewSortByStatusAscending, TaskListViewSortByPriorityAscending, TaskUpdateView,
                         TaskListViewSortByDeadlineAscending, TaskListViewSortByDeadlineDescending,
                         TaskListViewSortByPriorityDescending, TaskListViewSortByStatusDescending,
                         TaskListViewSortByAssigneeDescending, TaskListViewSortBySprintDescending, home)
# from sprints.views import (SprintListView)

urlpatterns = [
    # path('', home, name='dashboard'), moved to main
    path('productbacklog/', TaskListView.as_view(), name='product-backlog'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    path('productbacklog/sortby/sprint/ascending', TaskListViewSortBySprintAscending.as_view(), name='sort-by-sprint-ascending'),
    path('productbacklog/sortby/assignee/ascending', TaskListViewSortByAssigneeAscending.as_view(), name='sort-by-assignee-ascending'),
    path('productbacklog/sortby/status/ascending', TaskListViewSortByStatusAscending.as_view(), name='sort-by-status-ascending'),
    path('productbacklog/sortby/priority/ascending', TaskListViewSortByPriorityAscending.as_view(), name='sort-by-priority-ascending'),
    path('productbacklog/sortby/due_date/ascending', TaskListViewSortByDeadlineAscending.as_view(), name='sort-by-deadline-ascending'),

    path('productbacklog/sortby/sprint/descending', TaskListViewSortBySprintDescending.as_view(), name='sort-by-sprint-descending'),
    path('productbacklog/sortby/assignee/descending', TaskListViewSortByAssigneeDescending.as_view(), name='sort-by-assignee-descending'),
    path('productbacklog/sortby/status/descending', TaskListViewSortByStatusDescending.as_view(), name='sort-by-status-descending'),
    path('productbacklog/sortby/priority/descending', TaskListViewSortByPriorityDescending.as_view(), name='sort-by-priority-descending'),
    path('productbacklog/sortby/due_date/descending', TaskListViewSortByDeadlineDescending.as_view(), name='sort-by-deadline-descending'),
]