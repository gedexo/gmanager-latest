from core.base import BaseTable
from django_tables2 import columns

from .models import Department, Designation, Employee, Grade, SubDepartment


class EmployeeTable(BaseTable):
    employee_id = columns.Column(linkify=True)

    class Meta:
        model = Employee
        fields = (
            "employee_id",
            "fullname",
            "department",
            "designation",
            "grade",
            "blood_group",
            "is_active",
        )
        attrs = {"class": "table key-buttons border-bottom"}


class DepartmentTable(BaseTable):
    class Meta:
        model = Department
        fields = ("name", "is_active")
        attrs = {"class": "table key-buttons border-bottom"}


class SubDepartmentTable(BaseTable):
    class Meta:
        model = SubDepartment
        fields = ("name", "department", "is_active")
        attrs = {"class": "table key-buttons border-bottom"}


class DesignationTable(BaseTable):
    class Meta:
        model = Designation
        fields = ("name", "is_active")
        attrs = {"class": "table key-buttons border-bottom"}


class GradeTable(BaseTable):
    class Meta:
        model = Grade
        fields = ("name", "is_active")
        attrs = {"class": "table key-buttons border-bottom"}
