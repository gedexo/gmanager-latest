from django.urls import path

from . import views

app_name = "hrms"

urlpatterns = [
    path("leave_type/", views.LeaveTypeListView.as_view(), name="leave_type_list"),
    path(
        "leave_type/<str:pk>/",
        views.LeaveTypeDetailView.as_view(),
        name="leave_type_detail",
    ),
    path("new/leave_type/", views.LeaveTypeCreateView.as_view(), name="leave_type_create"),
    path(
        "leave_type/<str:pk>/update/",
        views.LeaveTypeUpdateView.as_view(),
        name="leave_type_update",
    ),
    path(
        "leave_type/<str:pk>/delete/",
        views.LeaveTypeDeleteView.as_view(),
        name="leave_type_delete",
    ),
    path(
        "leave_request/",
        views.LeaveRequestListView.as_view(),
        name="leave_request_list",
    ),
    path(
        "leave_request/<str:pk>/",
        views.LeaveRequestDetailView.as_view(),
        name="leave_request_detail",
    ),
    path(
        "new/leave_request/",
        views.LeaveRequestCreateView.as_view(),
        name="leave_request_create",
    ),
    path(
        "leave_request/<str:pk>/update/",
        views.LeaveRequestUpdateView.as_view(),
        name="leave_request_update",
    ),
    path(
        "leave_request/<str:pk>/delete/",
        views.LeaveRequestDeleteView.as_view(),
        name="leave_request_delete",
    ),
    path(
        "leave_request/<str:pk>/approve/",
        views.LeaveRequestApproveView.as_view(),
        name="leave_request_approve",
    ),
    path(
        "leave_request/<str:pk>/reject/",
        views.LeaveRequestRejectView.as_view(),
        name="leave_request_reject",
    ),
    path("attendance/", views.AttendanceListView.as_view(), name="attendance_list"),
    path(
        "attendance/<str:pk>/",
        views.AttendanceDetailView.as_view(),
        name="attendance_detail",
    ),
    path(
        "new/attendance/",
        views.AttendanceCreateView.as_view(),
        name="attendance_create",
    ),
    path(
        "attendance/<str:pk>/update/",
        views.AttendanceUpdateView.as_view(),
        name="attendance_update",
    ),
    path(
        "attendance/<str:pk>/delete/",
        views.AttendanceDeleteView.as_view(),
        name="attendance_delete",
    ),
]
