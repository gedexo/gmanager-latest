from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
    path("task/<str:pk>/", views.TaskDetailView.as_view(), name="task_detail"),
    path("new/task/", views.TaskCreateView.as_view(), name="task_create"),
    path("task/<str:pk>/update/", views.TaskUpdateView.as_view(), name="task_update"),
    path("task/<str:pk>/review/", views.TaskReviewView.as_view(), name="task_review"),
    path(
        "task/<str:pk>/on_going/",
        views.TaskInProgressView.as_view(),
        name="task_on_going",
    ),
    path("task/<str:pk>/done/", views.TaskDoneView.as_view(), name="task_done"),
    path("task/<str:pk>/delete/", views.TaskDeleteView.as_view(), name="task_delete"),
    path("reminder/", views.ReminderListView.as_view(), name="reminder_list"),
    path("reminder/<str:pk>/", views.ReminderDetailView.as_view(), name="reminder_detail"),
    path("new/reminder/", views.ReminderCreateView.as_view(), name="reminder_create"),
    path(
        "reminder/<str:pk>/update/",
        views.ReminderUpdateView.as_view(),
        name="reminder_update",
    ),
    path(
        "reminder/<str:pk>/delete/",
        views.ReminderDeleteView.as_view(),
        name="reminder_delete",
    ),
    path("task/<str:pk>/update_status/", views.task_update, name="task_update_status"),
    path(
        "task/<str:pk>/update_remarks/",
        views.task_remark_update,
        name="task_remark_update",
    ),
]
