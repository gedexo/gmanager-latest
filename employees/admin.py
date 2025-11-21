from core.base import BaseAdmin
from django.contrib import admin

from .models import Department, Designation, Employee, Grade, SubDepartment


@admin.register(Department)
class DepartmentAdmin(BaseAdmin):
    list_display = ("name", "description", "is_active", "employee_count")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    ordering = ("name",)
    autocomplete_fields = ("department_lead",)


@admin.register(SubDepartment)
class SubDepartmentAdmin(BaseAdmin):
    list_display = ("name", "department", "description", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    ordering = ("name",)


@admin.register(Designation)
class DesignationAdmin(BaseAdmin):
    list_display = ("name", "description", "is_active", "employee_count")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    ordering = ("name",)


@admin.register(Grade)
class GradeAdmin(BaseAdmin):
    list_display = ("name", "description", "is_active", "employee_count")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    ordering = ("name",)


@admin.register(Employee)
class EmployeeAdmin(BaseAdmin):
    list_display = (
        "employee_id",
        "user",
        "fullname",
        "department",
        "designation",
        "grade",
        "blood_group",
        "is_active",
    )
    list_filter = ("is_active", "department", "designation", "grade")
    search_fields = (
        "user__username",
        "employee_id",
        "first_name",
        "middle_name",
        "last_name",
    )
    ordering = ("user__first_name", "user__last_name")
    autocomplete_fields = ("user", "department", "designation", "grade")
