from core.base import BaseModel
from django.db import models
from django.urls import reverse_lazy
from tinymce.models import HTMLField


class Course(BaseModel):
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    what_will_i_learn = HTMLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to="courses", null=True, blank=True)
    department = models.ForeignKey("employees.Department", on_delete=models.CASCADE, null=True, blank=True)
    preview_video = models.CharField(max_length=128, null=True, blank=True)

    def get_groups(self):
        return self.group_set.all()

    def get_absolute_url(self):
        return reverse_lazy("lms:course_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("lms:course_list")

    def __str__(self):
        return self.title


class Group(BaseModel):
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["course", "order"]

    def get_resources(self):
        return self.resource_set.all()

    def __str__(self):
        return self.title


class Resource(BaseModel):
    title = models.CharField(max_length=128, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    video_id = models.CharField(max_length=128, null=True, blank=True)
    content = HTMLField(null=True, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["group__course", "group", "order"]

    def get_absolute_url(self):
        return reverse_lazy("lms:resource_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
