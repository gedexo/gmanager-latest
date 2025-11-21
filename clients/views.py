from core import mixins
from django.urls import reverse_lazy

from . import tables
from .models import Client


class ClientListView(mixins.HybridListView):
    model = Client
    table_class = tables.ClientTable
    filterset_fields = ("fullname",)
    permissions = ("management", "hrm", "marketing")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Clients"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm", "marketing"))
        context["new_link"] = reverse_lazy("clients:client_create")
        return context


class ClientDetailView(mixins.HybridDetailView):
    model = Client
    permissions = ("management", "hrm", "marketing")


class ClientCreateView(mixins.HybridCreateView):
    model = Client
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm", "marketing")


class ClientUpdateView(mixins.HybridUpdateView):
    model = Client
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm", "marketing")


class ClientDeleteView(mixins.HybridDeleteView):
    model = Client
    permissions = ("management", "hrm", "marketing")
