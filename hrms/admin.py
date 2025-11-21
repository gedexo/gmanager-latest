from core.base import BaseAdmin
from django.contrib import admin

from .models import Attendance, LeaveRequest, LeaveType


@admin.register(LeaveType)
class LeaveTypeAdmin(BaseAdmin):
    list_display = ("name", "description", "max_days", "is_paid")
    search_fields = ("name", "description")


@admin.register(LeaveRequest)
class LeaveRequestAdmin(BaseAdmin):
    list_display = ("employee", "leave_type", "start_date", "end_date", "status")
    search_fields = ("employee", "start_date", "end_date", "status")
    list_filter = ("employee", "leave_type", "start_date", "end_date", "status")
    autocomplete_fields = ("employee", "leave_type")


@admin.register(Attendance)
class AttendanceAdmin(BaseAdmin):
    list_display = ("employee", "date", "status", "time_in", "time_out")
    list_filter = ("employee", "date", "status")
    autocomplete_fields = ("employee",)
