from core import mixins
from django.urls import reverse_lazy
from marketing.models import Enquiry
from projects.models import Project
from projects.tables import ProjectStaffTable, ProjectTable
from tasks.models import Task


class HomeView(mixins.HybridListView):
    model = Project
    table_class = ProjectTable
    filterset_fields = ("name", "client", "start_date", "end_date")
    permissions = (
        "management",
        "hrm",
        "marketing",
        "accounts",
        "hod",
        "worker",
        "client",
    )
    template_name = "core/home.html"

    def get_table_class(self):
        if self.request.user.usertype == "worker":
            return ProjectStaffTable
        return ProjectTable
    
    def get_tasks(self):
        if self.request.user.usertype in ("management", "hrm", "accounts"):
            return Task.objects.filter(is_active=True)
        elif self.request.user.usertype == "hod":
            return Task.objects.filter(
                is_active=True,
                assigned_to__department=self.request.user.employee.department,
            )
        else:
            return Task.objects.filter(is_active=True, assigned_to=self.request.user.employee)

    def get_queryset(self):
        if self.request.user.usertype in ("management", "hrm", "accounts"):
            return self.model.objects.filter(is_active=True)
        elif self.request.user.usertype == "hod":
            return self.model.objects.filter(is_active=True, department=self.request.user.employee.department)
        if self.request.user.usertype == "worker":
            tasks = Task.objects.filter(is_active=True, assigned_to=self.request.user.employee)
            projects = Project.objects.filter(task__in=tasks).distinct()
            return self.model.objects.filter(is_active=True, id__in=projects)
        elif self.request.user.usertype == "client":
            return self.model.objects.filter(client=self.request.user.client)
        else:
            return self.model.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usertype = self.request.user.usertype
        context["title"] = "Enquiries"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm", "marketing"))
        context["new_link"] = reverse_lazy("marketing:enquiry_create")
        context["todo_tasks_count"] = self.get_tasks().filter(status="todo").count()
        context["on_going_tasks_count"] = self.get_tasks().filter(status="on_going").count()
        context["on_hold_tasks_count"] = self.get_tasks().filter(status="on_hold").count()
        context["delayed_tasks_count"] = self.get_tasks().filter(status="delayed").count()
        context["in_review_tasks_count"] = self.get_tasks().filter(status="in_review").count()
        context["completed_tasks_count"] = self.get_tasks().filter(status="done").count()
        context["cancelled_tasks_count"] = self.get_tasks().filter(status="cancelled").count()
        context["rework_tasks_count"] = self.get_tasks().filter(status="rework").count()

        if usertype in ("management", "hrm", "hod"):
            context["open_enquiries_count"] = Enquiry.objects.filter(status="open").count()
            context["closed_enquiries_count"] = Enquiry.objects.filter(status="closed").count()
            context["rejected_enquiries_count"] = Enquiry.objects.filter(status="rejected").count()
            context["estimate_sent_enquiries_count"] = Enquiry.objects.filter(status="estimate_sent").count()
            context["todo_projects_count"] = Project.objects.filter(status="todo").count()
            context["on_going_projects_count"] = Project.objects.filter(status="on_going").count()
            context["in_review_projects_count"] = Project.objects.filter(status="in_review").count()
            context["done_projects_count"] = Project.objects.filter(status__in=("done", "delivered")).count()
        return context
