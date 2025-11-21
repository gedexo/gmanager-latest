from core.base import BaseTable

from .models import Course


class CourseTable(BaseTable):
    created = None

    class Meta:
        model = Course
        fields = ("title", "department")
        attrs = {"class": "table key-buttons border-bottom"}
