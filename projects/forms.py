from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ("creator", "is_active")
        widgets = {
            'start_date': forms.TextInput(attrs={'class': 'flatpicker form-control'}),
            'end_date': forms.TextInput(attrs={'class': 'flatpicker form-control'}),
            'delivery_date': forms.TextInput(attrs={'class': 'flatpicker form-control'}),
        }