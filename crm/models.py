from core.base import BaseModel
from django.db import models


class Lead(BaseModel):
    phone = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    label = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        choices=(("Hot", "Hot"), ("Cold", "Cold"), ("Warm", "Warm")),
    )
    expected_close_date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=255, default="Lead", choices=(("Lead", "Lead"), ("Deal", "Deal")))
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Leads"

    def __str__(self):
        return self.contact_person
