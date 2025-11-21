from core.base import BaseAdmin
from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(BaseAdmin):
    list_display = (
        "contact_person",
        "company_name",
        "title",
        "value",
        "label",
        "expected_close_date",
        "phone",
        "email",
        "status",
    )
    list_filter = ("label", "status")
    search_fields = (
        "contact_person",
        "company_name",
        "title",
        "value",
        "label",
        "expected_close_date",
        "phone",
        "email",
        "status",
    )
