from core import mixins
from django.urls import reverse_lazy

from . import tables
from .models import Attendance, LeaveRequest, LeaveType


class LeaveTypeListView(mixins.HybridListView):
    model = LeaveType
    table_class = tables.LeaveTypeTable
    filterset_fields = []
    permissions = ("management", "hrm")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Leave Types"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm"))
        context["new_link"] = reverse_lazy("hrms:leave_type_create")
        return context


class LeaveTypeDetailView(mixins.HybridDetailView):
    model = LeaveType
    permissions = ("management", "hrm")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Leave Type"
        return context


class LeaveTypeCreateView(mixins.HybridCreateView):
    model = LeaveType
    exclude = ("name",)
    permissions = ("management", "hrm")

    def get_success_url(self):
        return reverse_lazy("hrms:leave_type_list")


class LeaveTypeUpdateView(mixins.HybridUpdateView):
    model = LeaveType
    fields = ("name",)
    permissions = ("management", "hrm")

    def get_success_url(self):
        return reverse_lazy("hrms:leave_type_list")


class LeaveTypeDeleteView(mixins.HybridDeleteView):
    model = LeaveType
    permissions = ("management", "hrm")

    def get_success_url(self):
        return reverse_lazy("hrms:leave_type_list")


class LeaveRequestListView(mixins.HybridListView):
    model = LeaveRequest
    table_class = tables.LeaveRequestTable
    filterset_fields = ["employee", "status"]
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Leave Requests"
        context["can_add"] = mixins.check_access(
            self.request,
            ("management", "hrm", "accounts", "hod", "marketing", "worker"),
        )
        context["new_link"] = reverse_lazy("hrms:leave_request_create")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if mixins.check_access(self.request, ("management", "hrm")):
            return queryset
        elif mixins.check_access(self.request, ("hod")):
            return queryset.filter(employee__department=self.request.user.employee.department)
        else:
            return queryset.filter(employee=self.request.user.employee)


class LeaveRequestDetailView(mixins.HybridDetailView):
    model = LeaveRequest
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Leave Request"
        return context


class LeaveRequestCreateView(mixins.HybridCreateView):
    model = LeaveRequest
    fields = ("leave_type", "start_date", "end_date", "reason")
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_success_url(self):
        return reverse_lazy("hrms:leave_request_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Leave Request"
        return context

    def form_valid(self, form):
        form.instance.employee = self.request.user.employee
        return super().form_valid(form)


class LeaveRequestUpdateView(mixins.HybridUpdateView):
    model = LeaveRequest
    fields = ("leave_type", "start_date", "end_date")
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_success_url(self):
        return reverse_lazy("hrms:leave_request_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Leave Request"
        return context


class LeaveRequestDeleteView(mixins.HybridDeleteView):
    model = LeaveRequest
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_success_url(self):
        return reverse_lazy("hrms:leave_request_list")


class LeaveRequestApproveView(mixins.HybridUpdateView):
    model = LeaveRequest
    fields = ("status",)
    permissions = ("management", "hrm")

    def get_success_url(self):
        return reverse_lazy("hrms:leave_request_list")


class LeaveRequestRejectView(mixins.HybridUpdateView):
    model = LeaveRequest
    fields = ("status",)
    permissions = ("management", "hrm")

    def get_success_url(self):
        return reverse_lazy("hrms:leave_request_list")


class AttendanceListView(mixins.HybridListView):
    model = Attendance
    table_class = tables.AttendanceTable
    filterset_fields = ["employee", "date"]
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Attendances"
        context["can_add"] = mixins.check_access(
            self.request,
            ("management", "hrm", "accounts", "hod", "marketing", "worker"),
        )
        context["new_link"] = reverse_lazy("hrms:attendance_create")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if mixins.check_access(self.request, ("management", "hrm")):
            return queryset
        elif mixins.check_access(self.request, ("hod")):
            return queryset.filter(employee__department=self.request.user.employee.department)
        else:
            return queryset.filter(employee=self.request.user.employee)


class AttendanceDetailView(mixins.HybridDetailView):
    model = Attendance
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Attendance"
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if mixins.check_access(self.request, ("management", "hrm")):
            return queryset
        elif mixins.check_access(self.request, ("hod")):
            return queryset.filter(employee__department=self.request.user.employee.department)
        else:
            return queryset.filter(employee=self.request.user.employee)


class AttendanceCreateView(mixins.HybridCreateView):
    model = Attendance
    fields = ("employee", "date", "time_in", "time_out", "status", "remarks")
    permissions = ("hrm",)

    def get_success_url(self):
        return reverse_lazy("hrms:attendance_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Attendance"
        return context


class AttendanceUpdateView(mixins.HybridUpdateView):
    model = Attendance
    fields = ("employee", "date", "time_in", "time_out", "status", "remarks")
    permissions = ("hrm",)

    def get_success_url(self):
        return reverse_lazy("hrms:attendance_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Attendance"
        return context


class AttendanceDeleteView(mixins.HybridDeleteView):
    model = Attendance
    permissions = ("hrm",)

    def get_success_url(self):
        return reverse_lazy("hrms:attendance_list")
