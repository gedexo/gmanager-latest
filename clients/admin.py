from core.base import BaseAdmin
from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(BaseAdmin):
    list_display = ("fullname", "user", "email", "phone", "address", "is_active")
    list_filter = ("is_active",)
    search_fields = ("fullname", "email", "phone", "address")
    ordering = ("fullname",)
