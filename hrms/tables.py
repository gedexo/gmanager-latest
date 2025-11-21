from core.base import BaseTable
from django_tables2 import columns

from .models import Attendance, LeaveRequest, LeaveType


class LeaveTypeTable(BaseTable):
    name = columns.Column(linkify=True)

    class Meta:
        model = LeaveType
        fields = ("name",)
        attrs = {"class": "table key-buttons border-bottom"}


class LeaveRequestTable(BaseTable):
    employee = columns.Column(linkify=True)

    class Meta:
        model = LeaveRequest
        fields = ("employee", "leave_type", "start_date", "end_date", "status")
        attrs = {"class": "table key-buttons border-bottom"}


class AttendanceTable(BaseTable):
    employee = columns.Column(linkify=True)

    class Meta:
        model = Attendance
        fields = ("employee", "date", "status", "time_in", "time_out")
        attrs = {"class": "table key-buttons border-bottom"}
