from core.base import BaseModel
from django.db import models
from django.urls import reverse_lazy


class Enquiry(BaseModel):
    STATUS_CHOICES = (
        ("open", "Open"),
        ("estimate_sent", "Estimate Sent"),
        ("closed", "Closed"),
        ("rejected", "Rejected"),
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="open")
    department = models.ForeignKey("employees.Department", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Enquiries"

    def get_badge(self):
        if self.status == "open":
            return "badge-primary"
        elif self.status == "closed":
            return "badge-success"
        elif self.status == "rejected":
            return "badge-danger"
        return None

    def get_absolute_url(self):
        return reverse_lazy("marketing:enquiry_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("marketing:enquiry_list")

    def get_update_url(self):
        return reverse_lazy("marketing:enquiry_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("marketing:enquiry_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)


class EnquiryFollowup(BaseModel):
    enquiry = models.ForeignKey("marketing.Enquiry", on_delete=models.CASCADE)
    details = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=255,
        choices=(("open", "Open"), ("closed", "Closed"), ("rejected", "Rejected")),
        default="open",
    )

    class Meta:
        verbose_name_plural = "Enquiry Followups"
        ordering = ("-created",)

    def get_badge(self):
        if self.status == "open":
            return "badge-primary"
        elif self.status == "closed":
            return "badge-success"
        elif self.status == "rejected":
            return "badge-danger"
        return None

    def get_absolute_url(self):
        return reverse_lazy("marketing:enquiryfollowup_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("marketing:enquiryfollowup_list")

    def get_update_url(self):
        return reverse_lazy("marketing:enquiryfollowup_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("marketing:enquiryfollowup_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.details)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        last_followup = EnquiryFollowup.objects.filter(enquiry=self.enquiry).order_by("-created").first()
        if last_followup:
            self.enquiry.status = last_followup.status
            self.enquiry.save()
