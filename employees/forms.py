from django import forms
from django.forms import widgets
from employees.models import Employee


class ImageForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("photo",)
        widgets = {"photo": widgets.FileInput(attrs={"class": "form-control-file d-none"})}
