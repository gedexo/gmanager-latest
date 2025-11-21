from core import mixins
from django.urls import reverse_lazy

from . import tables
from .models import User


class UserListView(mixins.HybridListView):
    model = User
    table_class = tables.UserTable
    filterset_fields = ("usertype", "is_active", "is_staff")
    permissions = ("management", "hrm")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Users"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm"))
        context["new_link"] = reverse_lazy("accounts:user_create")
        return context


class UserDetailView(mixins.HybridDetailView):
    model = User
    permissions = ("management", "hrm")


class UserCreateView(mixins.HybridCreateView):
    model = User
    exclude = (
        "is_active",
        "date_joined",
        "user_permissions",
        "groups",
        "last_login",
        "is_superuser",
        "is_staff",
    )
    permissions = ("management", "hrm")

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data["password"])
        return super().form_valid(form)


class UserUpdateView(mixins.HybridUpdateView):
    model = User
    exclude = (
        "is_active",
        "password",
        "date_joined",
        "user_permissions",
        "groups",
        "last_login",
        "is_superuser",
        "is_staff",
    )
    permissions = ("management", "hrm")


class UserDeleteView(mixins.HybridDeleteView):
    model = User
    permissions = ("management", "hrm")
