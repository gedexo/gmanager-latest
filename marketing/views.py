from core import mixins
from django.shortcuts import redirect
from django.urls import reverse_lazy

from . import tables
from .forms import EnquiryFollowupForm
from .models import Enquiry, EnquiryFollowup


class EnquiryListView(mixins.HybridListView):
    model = Enquiry
    table_class = tables.EnquiryTable
    filterset_fields = ("name", "status")
    permissions = ("management", "accounts", "marketing", "hod")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Enquiries"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm", "marketing"))
        context["new_link"] = reverse_lazy("marketing:enquiry_create")
        context["open_enquiries_count"] = Enquiry.objects.filter(status="open").count()
        context["closed_enquiries_count"] = Enquiry.objects.filter(status="closed").count()
        context["rejected_enquiries_count"] = Enquiry.objects.filter(status="rejected").count()
        context["estimate_sent_enquiries_count"] = Enquiry.objects.filter(status="estimate_sent").count()
        return context


class EnquiryDetailView(mixins.HybridDetailView):
    model = Enquiry
    permissions = ("management", "accounts", "marketing", "hod")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["followups"] = EnquiryFollowup.objects.filter(enquiry=self.object)
        context["form"] = EnquiryFollowupForm()
        return context

    def form_valid(self, form):
        enquiry = self.get_object()
        followup = form.save(commit=False)
        followup.enquiry = enquiry
        followup.save()
        return redirect(self.get_success_url())


class EnquiryCreateView(mixins.HybridCreateView):
    model = Enquiry
    exclude = ("creator", "is_active")
    permissions = ("management", "accounts", "marketing", "hod")

    def get_success_url(self):
        return reverse_lazy("marketing:enquiry_detail", kwargs={"pk": self.object.pk})


class EnquiryUpdateView(mixins.HybridUpdateView):
    model = Enquiry
    exclude = ("creator", "is_active")
    permissions = ("management", "accounts", "marketing", "hod")

    def get_success_url(self):
        return reverse_lazy("marketing:enquiry_detail", kwargs={"pk": self.object.pk})


class EnquiryDeleteView(mixins.HybridDeleteView):
    model = Enquiry
    permissions = ("management", "accounts", "marketing", "hod")


class EnquiryFollowupListView(mixins.HybridListView):
    model = EnquiryFollowup
    table_class = tables.EnquiryFollowupTable
    filterset_fields = ("details",)
    permissions = ("management", "accounts", "marketing", "hod")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.user
        context["title"] = "Enquiry Followups"
        context["can_add"] = mixins.check_access(self.request, ("management", "hrm", "marketing"))
        context["new_link"] = reverse_lazy("marketing:enquiryfollowup_create")
        return context


class EnquiryFollowupDetailView(mixins.HybridDetailView):
    model = EnquiryFollowup
    permissions = ("management", "accounts", "marketing", "hod")


class EnquiryFollowupCreateView(mixins.HybridCreateView):
    model = EnquiryFollowup
    exclude = ("creator", "is_active")
    permissions = ("management", "accounts", "marketing", "hod")

    def get_success_url(self):
        return reverse_lazy("marketing:enquiry_detail", kwargs={"pk": self.object.enquiry.pk})


class EnquiryFollowupUpdateView(mixins.HybridUpdateView):
    model = EnquiryFollowup
    exclude = ("creator", "is_active")
    permissions = ("management", "accounts", "marketing", "hod")


class EnquiryFollowupDeleteView(mixins.HybridDeleteView):
    model = EnquiryFollowup
    permissions = ("management", "accounts", "marketing", "hod")
