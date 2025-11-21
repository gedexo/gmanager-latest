import uuid

from clients.models import Client
from core.functions import generate_fields
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy
from employees.models import Employee


class User(AbstractUser):
    usertype = models.CharField(
        max_length=128,
        choices=[
            ("client", "Client"),
            ("management", "Management Staff"),
            ("hrm", "HRM Staff"),
            ("accounts", "Accounts Staff"),
            ("hod", "HOD Staff"),
            ("marketing", "Marketing Staff"),
            ("worker", "Worker Staff"),
        ],
        default="worker",
    )
    notification_id = models.CharField(max_length=128, null=True, blank=True, default=uuid.uuid4)

    def get_fields(self):
        return generate_fields(self)

    def get_absolute_url(self):
        return reverse_lazy("accounts:user_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("accounts:user_list")

    def get_update_url(self):
        return reverse_lazy("accounts:user_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("accounts:user_delete", kwargs={"pk": self.pk})

    @property
    def fullname(self):
        if self.usertype == "client":
            if Client.objects.filter(user=self).exists():
                return self.client.fullname
            else:
                return self.username
        elif Employee.objects.filter(user=self).exists():
            full_name_parts = [
                part
                for part in [
                    self.employee.first_name,
                    self.employee.middle_name,
                    self.employee.last_name,
                ]
                if part is not None
            ]
            return " ".join(full_name_parts)
        else:
            return self.username

    def __str__(self):
        if self.usertype == "client":
            if Client.objects.filter(user=self).exists():
                return self.client.fullname
            else:
                return self.username
        elif Employee.objects.filter(user=self).exists():
            full_name_parts = [
                part
                for part in [
                    self.employee.first_name,
                    self.employee.middle_name,
                    self.employee.last_name,
                ]
                if part is not None
            ]
            return " ".join(full_name_parts)
        else:
            return self.username

    def designation(self):
        if Employee.objects.filter(user=self).exists():
            return self.employee.designation
        else:
            return None
