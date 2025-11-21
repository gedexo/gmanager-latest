from core.base import BaseModel
from django.db import models
from django.urls import reverse_lazy


class Task(BaseModel):
    TASK_CHOICES = (
        ("todo", "To Do"),
        ("on_going", "On Going"),
        ("delayed", "On Going + Delay"),
        ("on_hold", "On Hold"),
        ("rework", "Rework"),
        ("cancelled", "Cancelled"),
        ("in_review", "In Review"),
        ("done", "Done"),
    )
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_from = models.DateField()
    end_before = models.DateField()
    assigned_to = models.ForeignKey("employees.Employee", on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=TASK_CHOICES)
    completed_on = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    rework_reason = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-status"]

    def get_absolute_url(self):
        return reverse_lazy("tasks:task_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("tasks:task_list")

    def get_update_url(self):
        return reverse_lazy("tasks:task_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("tasks:task_delete", kwargs={"pk": self.pk})

    def get_review_url(self):
        return reverse_lazy("tasks:task_review", kwargs={"pk": self.pk})

    def get_on_going_url(self):
        return reverse_lazy("tasks:task_on_going", kwargs={"pk": self.pk})

    def get_done_url(self):
        return reverse_lazy("tasks:task_done", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.title)


class Reminder(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=255, choices=(("Active", "Active"), ("Inactive", "Inactive")))

    def get_absolute_url(self):
        return reverse_lazy("tasks:reminder_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("tasks:reminder_list")

    def get_update_url(self):
        return reverse_lazy("tasks:reminder_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("tasks:reminder_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.title)
