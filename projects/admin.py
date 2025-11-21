from core.base import BaseAdmin
from django.contrib import admin
from tasks.models import Task

from .models import Project, ProjectAttachment


class ProjectAttachmentInline(admin.TabularInline):
    model = ProjectAttachment
    extra = 0
    exclude = ("creator", "is_active", "created", "updated")


class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    exclude = ("creator", "is_active", "created", "updated")

    class Media:
        js = ("extra_admin/js/project_task_inline.js",)


@admin.register(Project)
class ProjectAdmin(BaseAdmin):
    list_display = (
        "client",
        "name",
        "start_date",
        "end_date",
        "delivery_date",
        "department",
    )
    list_filter = (
        "is_active",
        "department",
        "client",
        "start_date",
        "end_date",
        "delivery_date",
    )
    search_fields = ("name", "client__fullname", "department__name")
    autocomplete_fields = ("client", "department")
    inlines = [TaskInline, ProjectAttachmentInline]
