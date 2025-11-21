from core.base import BaseTable
from django_tables2 import columns

from .models import Client


class ClientTable(BaseTable):
    fullname = columns.Column(linkify=True)

    class Meta:
        model = Client
        fields = ("fullname",)
        attrs = {"class": "table key-buttons border-bottom"}
