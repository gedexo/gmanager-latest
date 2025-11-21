from django import forms
from .models import Task
from projects.models import Project
from django.forms.models import inlineformset_factory

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'assigned_to', 'start_from', 'end_before', 'description', 'attachment', 'status')
        widgets = {
            'start_from': forms.DateInput(attrs={'class': 'flatpicker datetimeinput form-control'}),
            'end_before': forms.DateInput(attrs={'class': 'flatpicker datetimeinput form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Task title...'}),
            'assigned_to': forms.Select(attrs={'class': 'form-select select'}),
            'status': forms.Select(attrs={'class': 'form-select select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'attachment': forms.FileInput(attrs={'class': 'form-control form-control-sm'}),
        }

TaskFormSet = inlineformset_factory(
    Project,
    Task,
    form=TaskForm,
    extra=1,
    can_delete=True,
    fields=('title', 'assigned_to', 'start_from', 'end_before', 'description', 'attachment', 'status')
)