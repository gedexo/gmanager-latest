from django import forms

from .models import EnquiryFollowup


class EnquiryFollowupForm(forms.ModelForm):
    class Meta:
        model = EnquiryFollowup
        exclude = ("creator", "is_active", "enquiry")
