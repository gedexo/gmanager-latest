from django.urls import path

from . import views

app_name = "employees"

urlpatterns = [
    path("", views.EmployeeListView.as_view(), name="employee_list"),
    path("employee/<str:pk>/", views.EmployeeDetailView.as_view(), name="employee_detail"),
    path("new/employee/", views.EmployeeCreateView.as_view(), name="employee_create"),
    path(
        "employee/<str:pk>/update/",
        views.EmployeeUpdateView.as_view(),
        name="employee_update",
    ),
    path(
        "employee/<str:pk>/delete/",
        views.EmployeeDeleteView.as_view(),
        name="employee_delete",
    ),
    path("department/", views.DepartmentListView.as_view(), name="department_list"),
    path(
        "department/<str:pk>/",
        views.DepartmentDetailView.as_view(),
        name="department_detail",
    ),
    path(
        "new/department/",
        views.DepartmentCreateView.as_view(),
        name="department_create",
    ),
    path(
        "department/<str:pk>/update/",
        views.DepartmentUpdateView.as_view(),
        name="department_update",
    ),
    path(
        "department/<str:pk>/delete/",
        views.DepartmentDeleteView.as_view(),
        name="department_delete",
    ),
    path(
        "subdepartment/",
        views.SubDepartmentListView.as_view(),
        name="subdepartment_list",
    ),
    path(
        "subdepartment/<str:pk>/",
        views.SubDepartmentDetailView.as_view(),
        name="subdepartment_detail",
    ),
    path(
        "new/subdepartment/",
        views.SubDepartmentCreateView.as_view(),
        name="subdepartment_create",
    ),
    path(
        "subdepartment/<str:pk>/update/",
        views.SubDepartmentUpdateView.as_view(),
        name="subdepartment_update",
    ),
    path(
        "subdepartment/<str:pk>/delete/",
        views.SubDepartmentDeleteView.as_view(),
        name="subdepartment_delete",
    ),
    path("designation/", views.DesignationListView.as_view(), name="designation_list"),
    path(
        "designation/<str:pk>/",
        views.DesignationDetailView.as_view(),
        name="designation_detail",
    ),
    path(
        "new/designation/",
        views.DesignationCreateView.as_view(),
        name="designation_create",
    ),
    path(
        "designation/<str:pk>/update/",
        views.DesignationUpdateView.as_view(),
        name="designation_update",
    ),
    path(
        "designation/<str:pk>/delete/",
        views.DesignationDeleteView.as_view(),
        name="designation_delete",
    ),
    path("grade/", views.GradeListView.as_view(), name="grade_list"),
    path("grade/<str:pk>/", views.GradeDetailView.as_view(), name="grade_detail"),
    path("new/grade/", views.GradeCreateView.as_view(), name="grade_create"),
    path("grade/<str:pk>/update/", views.GradeUpdateView.as_view(), name="grade_update"),
    path("grade/<str:pk>/delete/", views.GradeDeleteView.as_view(), name="grade_delete"),
    path("profile/", views.ProfileView.as_view(), name="employee_profile"),
]
