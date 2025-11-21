import django_tables2 as tables
from core.base import BaseTable

from .models import Reminder, Task


class TaskTable(BaseTable):
    title = tables.columns.Column(linkify=True)
    created = None
    action = None
    status = tables.TemplateColumn(template_name="app/partials/task_status_form.html")
    quickview = tables.TemplateColumn(template_name="app/partials/task_view_modal.html")

    class Meta:
        model = Task
        fields = (
            "title",
            "quickview",
            "start_from",
            "end_before",
            "assigned_to",
            "completed_on",
            "status",
        )
        attrs = {"class": "table key-buttons border-bottom"}


class ReminderTable(BaseTable):
    title = tables.columns.Column(linkify=True)

    class Meta:
        model = Reminder
        fields = ("title",)
        attrs = {"class": "table key-buttons border-bottom"}
