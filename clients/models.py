from core.base import BaseModel
from django.db import models
from django.urls import reverse_lazy


class Client(BaseModel):
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        limit_choices_to={"usertype": "client"},
        blank=True,
        null=True,
    )
    fullname = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    enquiry = models.ForeignKey("marketing.Enquiry", on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy("clients:client_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("clients:client_list")

    def get_update_url(self):
        return reverse_lazy("clients:client_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("clients:client_delete", kwargs={"pk": self.pk})

    def __str__(self):
        return self.fullname
