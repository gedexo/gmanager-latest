from core.base import BaseModel
from django.db import models
from django.urls import reverse_lazy


class LeaveType(BaseModel):
    name = models.CharField(max_length=100)
    max_days = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)
    description = models.TextField()

    @staticmethod
    def get_list_url():
        return reverse_lazy("hrms:leave_type_list")

    def get_absolute_url(self):
        return reverse_lazy("hrms:leave_type_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("hrms:leave_type_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("hrms:leave_type_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)


class LeaveRequest(BaseModel):
    LEAVE_STATUS = (
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    )
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    remarks = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=LEAVE_STATUS, default="pending")

    @staticmethod
    def get_list_url():
        return reverse_lazy("hrms:leave_request_list")

    def get_absolute_url(self):
        return reverse_lazy("hrms:leave_request_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("hrms:leave_request_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("hrms:leave_request_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.employee)


class Attendance(BaseModel):
    STATUS_CHOICES = (
        ("present", "Present"),
        ("absent", "Absent"),
        ("unpaid_half_day", "Unpaid Half Day"),
        ("paid_half_day", "Paid Half Day"),
        ("unpaid_leave", "Unpaid Leave"),
        ("paid_leave", "Paid Leave"),
    )
    employee = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()
    status = models.CharField(max_length=20, default="present", choices=STATUS_CHOICES)
    remarks = models.TextField(blank=True, null=True)

    @staticmethod
    def get_list_url():
        return reverse_lazy("hrms:attendance_list")

    def get_absolute_url(self):
        return reverse_lazy("hrms:attendance_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("hrms:attendance_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("hrms:attendance_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.employee)
