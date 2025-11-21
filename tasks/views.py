from core import mixins
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from . import tables
from .models import Reminder, Task


class TaskListView(mixins.HybridListView):
    model = Task
    table_class = tables.TaskTable
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")
    filterset_fields = {
        "title": ["icontains"],
        "status": ["exact"],
        "start_from": ["gte"],
        "end_before": ["lte"],
        "assigned_to": ["exact"],
        "assigned_to__department": ["exact"],
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Tasks"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm", "hod"))
        context["new_link"] = reverse_lazy("tasks:task_create")
        context["todo_tasks_count"] = self.get_queryset().filter(status="todo").count()
        context["on_going_tasks_count"] = self.get_queryset().filter(status="on_going").count()
        context["on_hold_tasks_count"] = self.get_queryset().filter(status="on_hold").count()
        context["delayed_tasks_count"] = self.get_queryset().filter(status="delayed").count()
        context["in_review_tasks_count"] = self.get_queryset().filter(status="in_review").count()
        context["completed_tasks_count"] = self.get_queryset().filter(status="done").count()
        context["cancelled_tasks_count"] = self.get_queryset().filter(status="cancelled").count()
        context["rework_tasks_count"] = self.get_queryset().filter(status="rework").count()
        return context

    def get_queryset(self):
        if self.request.user.usertype in ("management", "hrm", "accounts"):
            return super().get_queryset()
        elif self.request.user.usertype == "hod":
            return super().get_queryset().filter(assigned_to__department=self.request.user.employee.department)
        else:
            return super().get_queryset().filter(assigned_to=self.request.user.employee)


class TaskDetailView(mixins.HybridDetailView):
    model = Task
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_queryset(self):
        if self.request.user.usertype in ("management", "hrm", "accounts"):
            return super().get_queryset()
        elif self.request.user.usertype == "hod":
            return super().get_queryset().filter(assigned_to__department=self.request.user.employee.department)
        else:
            return super().get_queryset().filter(assigned_to=self.request.user.employee)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm", "hod"))
        context["new_link"] = reverse("tasks:task_create")
        return context

class TaskCreateView(mixins.HybridCreateView):
    model = Task
    exclude = ("creator", "is_active", "completed_on")
    permissions = ("hrm", "hod", "management")

    def get_success_url(self):
        return reverse_lazy("tasks:task_detail", kwargs={"pk": self.object.pk})


class TaskUpdateView(mixins.HybridUpdateView):
    model = Task
    exclude = ("creator", "is_active", "completed_on")
    permissions = ("hrm", "hod", "management")

    def get_success_url(self):
        return reverse_lazy("tasks:task_detail", kwargs={"pk": self.object.pk})


class TaskInProgressView(mixins.HybridView):
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        task = Task.objects.get(pk=pk)
        if task.assigned_to == self.request.user.employee:
            task.status = "on_going"
            task.save()
            return JsonResponse({"status": "success", "message": task.status})
        else:
            return JsonResponse({"status": "failed"})


class TaskReviewView(mixins.HybridView):
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs.get("pk"))
        if task.assigned_to == self.request.user.employee:
            task.status = "in_review"
            task.save()
            return JsonResponse({"status": "success", "message": task.status})
        else:
            return JsonResponse({"status": "failed"})


class TaskDoneView(mixins.HybridView):
    permissions = ("hod", "management", "hrm")

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs.get("pk"))
        if task.assigned_to == self.request.user.employee:
            task.status = "done"
            task.save()
            return JsonResponse({"status": "success", "message": task.status})
        else:
            return JsonResponse({"status": "failed"})


class TaskDeleteView(mixins.HybridDeleteView):
    model = Task
    permissions = ("hrm", "hod", "management")


class ReminderListView(mixins.HybridListView):
    model = Reminder
    table_class = tables.ReminderTable
    filterset_fields = ("title",)
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Reminders"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm"))
        context["new_link"] = reverse_lazy("accounts:user_create")
        return context


class ReminderDetailView(mixins.HybridDetailView):
    model = Reminder
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")


class ReminderCreateView(mixins.HybridCreateView):
    model = Reminder
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")


class ReminderUpdateView(mixins.HybridUpdateView):
    model = Reminder
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")


class ReminderDeleteView(mixins.HybridDeleteView):
    model = Reminder
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")


def task_update(request, pk):
    crt_status = request.POST.get("status")
    task = get_object_or_404(Task, pk=pk)
    task.status = crt_status
    task.completed_on = timezone.now() if crt_status == "done" else None
    task.save()
    return JsonResponse({"status": "success"})


def task_remark_update(request, pk):
    remarks = request.POST.get("remarks")
    print(remarks)
    task = get_object_or_404(Task, pk=pk)
    task.remarks = remarks
    task.save()
    return JsonResponse({"status": "success"})
