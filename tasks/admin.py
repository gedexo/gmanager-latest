from core.base import BaseAdmin
from django.contrib import admin

from .models import Reminder, Task


@admin.register(Task)
class TaskAdmin(BaseAdmin):
    list_display = (
        "project",
        "title",
        "description",
        "start_from",
        "end_before",
        "assigned_to",
        "status",
        "completed_on",
    )
    list_filter = (
        "is_active",
        "status",
        "assigned_to",
        "project",
        "project__department",
    )
    search_fields = (
        "title",
        "description",
        "project__name",
        "assigned_to__user__first_name",
        "assigned_to__user__last_name",
    )
    autocomplete_fields = ("project", "assigned_to")


@admin.register(Reminder)
class ReminderAdmin(BaseAdmin):
    list_display = ("title", "description", "date", "time", "status")
    list_filter = ("is_active", "status")
    search_fields = ("title", "description")
