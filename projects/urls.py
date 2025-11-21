from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="project_list"),
    path("project/<str:pk>/", views.ProjectDetailView.as_view(), name="project_detail"),
    path("new/project/", views.ProjectCreateView.as_view(), name="project_create"),
    path(
        "project/<str:pk>/update/",
        views.ProjectUpdateView.as_view(),
        name="project_update",
    ),
    path(
        "project/<str:pk>/delete/",
        views.ProjectDeleteView.as_view(),
        name="project_delete",
    ),
    path(
        "attachment/<str:pk>/delete/",
        views.ProjectAttachmentDeleteView.as_view(),
        name="project_attachment_delete",
    ),
    path("project/<str:pk>/update_status/", views.project_update, name="project_update_status"),
]
