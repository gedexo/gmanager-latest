from core.base import BaseAdmin
from django.contrib import admin

from .models import Enquiry, EnquiryFollowup


class EnquiryFollowupInline(admin.TabularInline):
    model = EnquiryFollowup
    extra = 0


@admin.register(Enquiry)
class EnquiryAdmin(BaseAdmin):
    list_display = ("name", "phone", "email", "address", "details", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "phone", "email", "address", "details")
    inlines = (EnquiryFollowupInline,)


@admin.register(EnquiryFollowup)
class EnquiryFollowupAdmin(BaseAdmin):
    list_display = ("enquiry", "details", "status", "is_active", "created", "updated")
    list_filter = ("is_active", "status")
    search_fields = ("enquiry__name", "details")
    autocomplete_fields = ("enquiry",)
