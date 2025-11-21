from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from core import mixins
from django.urls import reverse
from tasks.models import Task
from tasks.tables import TaskTable

from . import tables
from .models import Project, ProjectAttachment


class ProjectListView(mixins.HybridListView):
    model = Project
    table_class = tables.ProjectTable
    permissions = ("management", "accounts", "hod", "worker", "client")
    filterset_fields = {
        "name": ["icontains"],
        "client": ["exact"],
        "start_date": ["gte"],
        "end_date": ["lte"],
        "status": ["exact"],
        "department": ["exact"],
    }
    template_name = "projects/project_list.html"

    def get_queryset(self):
        if self.request.user.usertype in ("management", "hrm", "accounts"):
            return self.model.objects.filter(is_active=True)
        if self.request.user.usertype == "worker":
            tasks = Task.objects.filter(is_active=True, assigned_to=self.request.user.employee)
            projects = Project.objects.filter(task__in=tasks).distinct()
            return self.model.objects.filter(is_active=True, id__in=projects)
        elif self.request.user.usertype == "client":
            return self.model.objects.filter(client=self.request.user.client)
        elif self.request.user.usertype == "hod":
            return self.model.objects.filter(is_active=True, department=self.request.user.employee.department)
        else:
            return self.model.objects.none()
    
    def get_table_class(self):
        if self.request.user.usertype == "worker":
            return tables.ProjectStaffTable
        return tables.ProjectTable
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Projects"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm", "hod"))
        context["new_link"] = reverse("projects:project_create")
        return context


class ProjectDetailView(mixins.HybridDetailView):
    model = Project
    permissions = ("management", "accounts", "hod", "worker", "client")

    def get_queryset(self):
        if self.request.user.usertype in ("management", "hrm", "accounts"):
            return self.model.objects.filter(is_active=True)
        if self.request.user.usertype == "worker":
            tasks = Task.objects.filter(is_active=True, assigned_to=self.request.user.employee)
            return Project.objects.filter(task__in=tasks).distinct()
        elif self.request.user.usertype == "client":
            return self.model.objects.filter(client=self.request.user.client)
        elif self.request.user.usertype == "hod":
            return self.model.objects.filter(is_active=True, department=self.request.user.employee.department)
        else:
            return self.model.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_object().name
        context["can_edit"] = mixins.check_access(self.request, ("management", "hrm", "hod"))
        context["can_delete"] = mixins.check_access(self.request, ("management", "hrm", "hod"))
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm", "hod"))
        context["new_link"] = reverse("tasks:task_create")
        context["table"] = TaskTable(self.get_tasks())
        context["tasks"] = self.get_tasks()
        context["attachments_table"] = tables.ProjectAttachmentTable(self.get_object().get_attachments())
        return context

    def get_tasks(self):
        if self.request.user.usertype in ("management", "hrm", "accounts"):
            return Task.objects.filter(is_active=True, project=self.get_object())
        if self.request.user.usertype == "hod":
            return Task.objects.filter(
                is_active=True,
                project=self.get_object(),
                project__department=self.request.user.employee.department,
            )
        elif self.request.user.usertype == "worker":
            return Task.objects.filter(
                is_active=True,
                project=self.get_object(),
                assigned_to=self.request.user.employee,
            )
        else:
            return Task.objects.none()


class ProjectCreateView(mixins.HybridCreateView):
    model = Project
    exclude = ("creator", "is_active")
    permissions = ("management", "accounts", "hod")


class ProjectUpdateView(mixins.HybridUpdateView):
    model = Project
    exclude = ("creator", "is_active")
    permissions = ("management", "accounts", "hod")

    def get_queryset(self):
        if self.request.user.usertype in ("management", "hrm", "accounts"):
            return self.model.objects.filter(is_active=True)
        if self.request.user.usertype == "worker":
            tasks = Task.objects.filter(assigned_to=self.request.user.employee, is_active=True)
            projects = Project.objects.filter(task__in=tasks).distinct()
            return self.model.objects.filter(is_active=True, id__in=projects)
        elif self.request.user.usertype == "client":
            return self.model.objects.filter(client=self.request.user.client)
        elif self.request.user.usertype == "hod":
            return self.model.objects.filter(is_active=True, department=self.request.user.employee.department)
        else:
            return self.model.objects.none()


class ProjectDeleteView(mixins.HybridDeleteView):
    model = Project
    permissions = ("management", "accounts", "hod")


class ProjectAttachmentDeleteView(mixins.HybridDeleteView):
    model = ProjectAttachment
    permissions = ("management", "accounts", "hod")


def project_update(request, pk):
    crt_status = request.POST.get("status")
    task = get_object_or_404(Project, pk=pk)
    task.status = crt_status
    task.delivery_date = timezone.now() if crt_status == "delivered" else None
    task.save()
    return JsonResponse({"status": "success"})