from django.conf import settings
from django.db.models import Q
from django.utils import timezone
from employees.models import Employee
from tasks.models import Task


def main_context(request):
    current_employee = None
    name = None
    app_settings = settings.APP_SETTINGS
    Task.objects.filter(Q(end_before__lt=timezone.now(), status="todo") | Q(end_before__lt=timezone.now(), status="on_going")).update(status="delayed")
    if request.user.is_authenticated and Employee.objects.filter(user=request.user).exists():
        current_employee = request.user.employee
        name = current_employee.first_name
    return {
        "current_employee": current_employee,
        "default_user_avatar": f"https://ui-avatars.com/api/?name={name}&background=fdc010&color=fff&size=128",
        "has_authority": request.user.is_authenticated and request.user.usertype in ("management", "hod"),
        "app_settings": app_settings,
    }
