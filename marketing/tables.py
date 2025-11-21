from core.base import BaseTable
from django_tables2 import columns

from .models import Enquiry, EnquiryFollowup


class EnquiryTable(BaseTable):
    name = columns.Column(linkify=True)

    class Meta:
        model = Enquiry
        fields = ("name", "phone", "creator", "department", "status")
        attrs = {"class": "table key-buttons border-bottom"}


class EnquiryFollowupTable(BaseTable):
    details = columns.Column(linkify=True)

    class Meta:
        model = EnquiryFollowup
        fields = ("details", "status")
        attrs = {"class": "table key-buttons border-bottom"}
