from core.base import BaseModel
from django.db import models
from django.urls import reverse_lazy
from tinymce.models import HTMLField


class Project(BaseModel):
    PROJECT_CHOICES = (
        ("todo", "To Do"),
        ("on_going", "On Going"),
        ("on_hold", "On Hold"),
        ("delayed", "On Going + Delay"),
        ("client_delayed", "Delay by Client"),
        ("in_review", "In Review"),
        ("cancelled", "Cancelled"),
        ("done", "Completed"),
        ("delivered", "Delivered"),
    )
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Project Name", max_length=255)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    department = models.ForeignKey("employees.Department", on_delete=models.CASCADE)
    subdepartment = models.ForeignKey("employees.SubDepartment", on_delete=models.CASCADE, blank=True, null=True)
    details = HTMLField(blank=True, null=True)
    referred_by = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="referred_by",
    )
    status = models.CharField(max_length=255, choices=PROJECT_CHOICES, default="todo")
    discord_url = models.URLField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("projects:project_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("projects:project_list")

    def get_update_url(self):
        return reverse_lazy("projects:project_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("projects:project_delete", kwargs={"pk": self.pk})

    def get_tasks(self):
        return self.task_set.filter(is_active=True)

    def get_attachments(self):
        return self.attachments.all()
    
    def tasks(self):
        return self.task_set.filter(is_active=True).count()

    def dones(self):
        return self.task_set.filter(is_active=True, status="done").count()
    def percentage(self):
        total = self.tasks()
        done = self.dones()
        if total == 0:
            return 0
        perc = int((done / total) * 100)
        return round(perc, 2)

    def __str__(self):
        return str(self.name)


class ProjectAttachment(BaseModel):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, related_name="attachments")
    title = models.CharField(max_length=255)
    attachment = models.FileField(upload_to="project_attachments")

    def __str__(self):
        return str(self.attachment)

    def get_delete_url(self):
        return reverse_lazy("projects:project_attachment_delete", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return str(self.title)
