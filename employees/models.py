import os
import uuid

from core.base import BaseModel
from core.choices import (
    BLOOD_CHOICES,
    EMPLOYMENT_TYPE_CHOICES,
    GENDER_CHOICES,
    MARITAL_CHOICES,
    RESIDENCE_CHOICES,
)
from django.db import models
from django.urls import reverse_lazy
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from versatileimagefield.fields import PPOIField, VersatileImageField


class Grade(BaseModel):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("employees:grade_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("employees:grade_list")

    def get_update_url(self):
        return reverse_lazy("employees:grade_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("employees:grade_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)

    def employee_count(self):
        return self.employee_set.filter(is_active=True).count()


class Designation(BaseModel):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("employees:designation_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("employees:designation_list")

    def get_update_url(self):
        return reverse_lazy("employees:designation_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("employees:designation_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)

    def employee_count(self):
        return self.employee_set.filter(is_active=True).count()


class Department(BaseModel):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    department_lead = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
        blank=True,
        null=True,
        related_name="department_lead",
    )

    def get_absolute_url(self):
        return reverse_lazy("employees:department_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("employees:department_list")

    def get_update_url(self):
        return reverse_lazy("employees:department_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("employees:department_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)

    def employee_count(self):
        return self.employee_set.filter(is_active=True).count()


class SubDepartment(BaseModel):
    department = models.ForeignKey(
        "employees.Department",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
        blank=True,
        null=True,
        related_name="sub_department",
    )
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("employees:subdepartment_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("employees:subdepartment_list")

    def get_update_url(self):
        return reverse_lazy("employees:subdepartment_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("employees:subdepartment_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)


class Employee(BaseModel):
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
        related_name="employee",
    )
    employee_id = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=300)
    middle_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    gender = models.CharField(max_length=128, choices=GENDER_CHOICES, blank=True, null=True)
    marital_status = models.CharField(max_length=128, choices=MARITAL_CHOICES, blank=True, null=True)
    personal_email = models.EmailField(max_length=128, blank=True, null=True)
    mobile = models.CharField(max_length=128, blank=True, null=True)
    whatsapp = models.CharField(max_length=128, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    religion = models.CharField(max_length=128, blank=True, null=True)
    photo = VersatileImageField(blank=True, null=True, upload_to="employees/photos/")
    ppoi = PPOIField("Image PPOI")

    # Company Info
    official_email = models.EmailField(max_length=128, blank=True, null=True)
    department = models.ForeignKey(
        "employees.Department",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
    )
    designation = models.ForeignKey(
        "employees.Designation",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
    )
    grade = models.ForeignKey(
        "employees.Grade",
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
    )

    # Parent Info
    father_name = models.CharField(max_length=128, blank=True, null=True)
    father_mobile = models.CharField(max_length=128, blank=True, null=True)
    mother_name = models.CharField(max_length=128, blank=True, null=True)
    guardian_name = models.CharField(max_length=128, blank=True, null=True)
    guardian_mobile = models.CharField(max_length=128, blank=True, null=True)
    relationship_with_employee = models.CharField(max_length=128, blank=True, null=True)

    # Dates
    date_of_joining = models.DateField(blank=True, null=True)
    date_of_confirmation = models.DateField(blank=True, null=True)

    # Residence Info
    type_of_residence = models.CharField(max_length=128, choices=RESIDENCE_CHOICES, blank=True, null=True)
    residence_name = models.CharField(max_length=128, blank=True, null=True)
    residential_address = models.TextField(blank=True, null=True)
    residence_contact = models.CharField(max_length=128, blank=True, null=True)
    residential_postal_code = models.CharField(max_length=128, blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    permanent_postal_code = models.CharField(max_length=128, blank=True, null=True)

    # Account Info

    bank_name = models.CharField(max_length=128, blank=True, null=True)
    account_name = models.CharField(max_length=128, blank=True, null=True)
    account_number = models.CharField("Bank Account Number", max_length=128, blank=True, null=True)
    ifsc_code = models.CharField("Bank IFSC Code", max_length=128, blank=True, null=True)
    bank_branch = models.CharField(max_length=128, blank=True, null=True)
    pan_number = models.CharField("PAN Card Number", max_length=128, blank=True, null=True)
    employment_type = models.CharField(max_length=128, choices=EMPLOYMENT_TYPE_CHOICES, blank=True, null=True)

    # Emergency Info
    blood_group = models.CharField(max_length=128, choices=BLOOD_CHOICES, blank=True, null=True)
    basic_salary = MoneyField(max_digits=14, decimal_places=2, default=Money(0, "INR"))
    hra = MoneyField(max_digits=14, decimal_places=2, default=Money(0, "INR"))
    other_allowance = MoneyField(max_digits=14, decimal_places=2, default=Money(0, "INR"))
    transportation_allowance = MoneyField(max_digits=14, decimal_places=2, default=Money(0, "INR"))

    def __str__(self):
        return self.fullname()

    def get_absolute_url(self):
        return reverse_lazy("employees:employee_detail", kwargs={"pk": self.pk})

    def get_image_url(self):
        if self.photo:
            return self.photo.url
        else:
            return f"https://ui-avatars.com/api/?name={self.first_name[:2]}&background=fdc010&color=fff&size=128"

    @staticmethod
    def get_list_url():
        return reverse_lazy("employees:employee_list")

    def get_update_url(self):
        return reverse_lazy("employees:employee_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("employees:employee_delete", kwargs={"pk": self.pk})

    def fullname(self):
        return f"{self.first_name} {self.last_name}" if self.last_name else self.first_name

    def is_hod_staff(self):
        return Department.objects.filter(department_lead=self).exists()

    def save(self, *args, **kwargs):
        if self.photo:
            self.photo.name = f"{uuid.uuid4()}{os.path.splitext(self.photo.name)[1]}"
        super().save(*args, **kwargs)
