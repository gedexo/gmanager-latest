from core.base import BaseAdmin
from django.contrib import admin

from .models import Course, Group, Resource


class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 0
    fields = ("order", "title", "video_id")


@admin.register(Course)
class CourseAdmin(BaseAdmin):
    list_display = ("title", "description", "department")
    list_filter = ("department",)


@admin.register(Group)
class GroupAdmin(BaseAdmin):
    list_display = ("title", "description", "course")
    list_filter = ("course",)
    inlines = [ResourceInline]


@admin.register(Resource)
class ResourceAdmin(BaseAdmin):
    list_display = ("title", "group", "video_id")
    list_filter = ("group",)
