from core import mixins
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from employees.models import Employee

from . import tables
from .forms import ImageForm
from .models import Department, Designation, Grade, SubDepartment


class DepartmentListView(mixins.HybridListView):
    model = Department
    table_class = tables.DepartmentTable
    filterset_fields = ("name",)
    permissions = ("management", "hrm", "hod", "accounts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Departments"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm"))
        context["new_link"] = reverse_lazy("employees:department_create")
        return context


class DepartmentDetailView(mixins.HybridDetailView):
    model = Department
    permissions = ("management", "hrm")


class DepartmentCreateView(mixins.HybridCreateView):
    model = Department
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm")


class DepartmentUpdateView(mixins.HybridUpdateView):
    model = Department
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm")


class DepartmentDeleteView(mixins.HybridDeleteView):
    model = Department
    permissions = ("management", "hrm")


class SubDepartmentListView(mixins.HybridListView):
    model = SubDepartment
    table_class = tables.SubDepartmentTable
    filterset_fields = ("name",)
    permissions = ("management", "hrm", "hod", "accounts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "SubDepartments"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm"))
        context["new_link"] = reverse_lazy("employees:subdepartment_create")
        return context


class SubDepartmentDetailView(mixins.HybridDetailView):
    model = SubDepartment
    permissions = ("management", "hrm")


class SubDepartmentCreateView(mixins.HybridCreateView):
    model = SubDepartment
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm")


class SubDepartmentUpdateView(mixins.HybridUpdateView):
    model = SubDepartment
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm")


class SubDepartmentDeleteView(mixins.HybridDeleteView):
    model = SubDepartment
    permissions = ("management", "hrm")


class GradeListView(mixins.HybridListView):
    model = Grade
    table_class = tables.GradeTable
    filterset_fields = ("name",)
    permissions = ("management", "hrm", "hod", "accounts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Grades"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm"))
        context["new_link"] = reverse_lazy("employees:grade_create")
        return context


class GradeDetailView(mixins.HybridDetailView):
    model = Grade
    permissions = ("management", "hrm")


class GradeCreateView(mixins.HybridCreateView):
    model = Grade
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm")


class GradeUpdateView(mixins.HybridUpdateView):
    model = Grade
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm")


class GradeDeleteView(mixins.HybridDeleteView):
    model = Grade
    permissions = ("management", "hrm")


class DesignationListView(mixins.HybridListView):
    model = Designation
    table_class = tables.DesignationTable
    filterset_fields = ("name",)
    permissions = ("management", "hrm", "hod", "accounts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Designations"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm"))
        context["new_link"] = reverse_lazy("employees:designation_create")
        return context


class DesignationDetailView(mixins.HybridDetailView):
    model = Designation
    permissions = ("management", "hrm")


class DesignationCreateView(mixins.HybridCreateView):
    model = Designation
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm")


class DesignationUpdateView(mixins.HybridUpdateView):
    model = Designation
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm")


class DesignationDeleteView(mixins.HybridDeleteView):
    model = Designation
    permissions = ("management", "hrm")


class EmployeeListView(mixins.HybridListView):
    model = Employee
    table_class = tables.EmployeeTable
    filterset_fields = ("department", "designation", "employment_type")
    permissions = ("management", "hrm", "hod", "accounts", "marketing", "worker")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employees"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm"))
        context["new_link"] = reverse_lazy("employees:employee_create")
        return context

    def get_queryset(self):
        if self.request.user.usertype in ("management", "hrm", "accounts"):
            return super().get_queryset()
        elif self.request.user.usertype == "hod":
            return super().get_queryset().filter(department=self.request.user.employee.department)
        else:
            return super().get_queryset().filter(pk=self.request.user.employee.pk)


class EmployeeDetailView(mixins.HybridDetailView):
    model = Employee
    permissions = ("management", "hrm", "hod", "accounts", "marketing", "worker")

    def get_queryset(self):
        if self.request.user.usertype in ("management", "hrm", "accounts"):
            return super().get_queryset()
        elif self.request.user.usertype == "hod":
            return super().get_queryset().filter(department=self.request.user.employee.department)
        else:
            return super().get_queryset().filter(pk=self.request.user.employee.pk)


class EmployeeCreateView(mixins.HybridCreateView):
    model = Employee
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm")


class EmployeeUpdateView(mixins.HybridUpdateView):
    model = Employee
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm")


class EmployeeDeleteView(mixins.HybridDeleteView):
    model = Employee
    permissions = ("management", "hrm")


class ProfileView(mixins.HybridDetailView):
    model = Employee
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")
    template_name = "employees/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Profile"
        context["image_form"] = ImageForm()
        return context

    def get_object(self, queryset=None):
        return self.request.user.employee

    def post(self, request, *args, **kwargs):
        instance = request.user.employee
        form = ImageForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": True})
        else:
            return HttpResponse("Invalid method")
