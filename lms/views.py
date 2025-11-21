from core import mixins

from . import tables
from .models import Course, Resource


class CourseListView(mixins.HybridListView):
    model = Course
    table_class = tables.CourseTable
    filterset_fields = ("department",)
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Courses"
        return context


class CourseDetailView(mixins.HybridDetailView):
    model = Course
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")


class ResourceDetailView(mixins.HybridDetailView):
    model = Resource
    permissions = ("management", "hrm", "accounts", "hod", "marketing", "worker")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.object.group.course
        return context
