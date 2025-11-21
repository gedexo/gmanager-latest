from core.base import BaseTable
from django_tables2 import columns
import django_tables2 as tables

from .models import Project, ProjectAttachment


class ProjectTable(BaseTable):
    name = columns.Column(linkify=True)
    created = None
    percentage = columns.TemplateColumn(
        """
        <div class='progress'>
            <div class='progress-bar' role='progressbar'
                style='width: {{ record.percentage }}%;' aria-valuenow='{{ record.percentage }}'
                aria-valuemin='0' aria-valuemax='100'>{{ record.percentage }}%
            </div>
        </div>
        """
    )
    tasks = columns.TemplateColumn(
        """{{record.dones}}/{{record.tasks}}
        """
    )
    status = tables.TemplateColumn(template_name="app/partials/project_status_form.html")
    class Meta:
        model = Project
        fields = (
            "name",
            "start_date",
            "end_date",
            "department",
            "status",
            "percentage",
            "tasks",
        )
        attrs = {"class": "table key-buttons border-bottom"}

class ProjectStaffTable(BaseTable):
    name = columns.Column(linkify=True)
    created = None
    percentage = columns.TemplateColumn(
        """
        <div class='progress'>
            <div class='progress-bar' role='progressbar'
                style='width: {{ record.percentage }}%;' aria-valuenow='{{ record.percentage }}'
                aria-valuemin='0' aria-valuemax='100'>{{ record.percentage }}%
            </div>
        </div>
        """
    )
    tasks = columns.TemplateColumn(
        """{{record.dones}}/{{record.tasks}}
        """
    )
    # status = tables.TemplateColumn(template_name="app/partials/project_status_form.html")
    class Meta:
        model = Project
        fields = (
            "name",
            "start_date",
            "end_date",
            "department",
            "status",
            "percentage",
            "tasks",
        )
        attrs = {"class": "table key-buttons border-bottom"}


class ProjectAttachmentTable(BaseTable):
    action = columns.TemplateColumn("<a href='{{ record.attachment.url }}' class='btn btn-sm btn-primary'>Download</a>")

    class Meta:
        model = ProjectAttachment
        fields = ("title",)
        attrs = {"class": "table key-buttons border-bottom"}
