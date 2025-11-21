from core import mixins
from django.urls import reverse_lazy
from django.http import JsonResponse

from . import tables
from .forms import ClientForm
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
    form_class = ClientForm

    def form_valid(self, form):
        self.object = form.save()
        
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'id': self.object.pk,
                'text': self.object.fullname,  
            })
        
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'errors': form.errors
            }, status=400)
        
        return super().form_invalid(form)


class ClientUpdateView(mixins.HybridUpdateView):
    model = Client
    exclude = ("creator", "is_active")
    permissions = ("management", "hrm", "marketing")


class ClientDeleteView(mixins.HybridDeleteView):
    model = Client
    permissions = ("management", "hrm", "marketing")
