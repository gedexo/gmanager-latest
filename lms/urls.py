from django.urls import path

from . import views

app_name = "lms"

urlpatterns = [
    path("courses/", views.CourseListView.as_view(), name="course_list"),
    path("courses/<str:pk>/", views.CourseDetailView.as_view(), name="course_detail"),
    path(
        "resources/<str:pk>/",
        views.ResourceDetailView.as_view(),
        name="resource_detail",
    ),
]
