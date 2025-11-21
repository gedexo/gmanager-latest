from core.base import BaseAdmin
from django.contrib import admin

from .models import Expense, ExpenseAccount, Income, IncomeAccount


@admin.register(ExpenseAccount)
class ExpenseAccountAdmin(BaseAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")


@admin.register(IncomeAccount)
class IncomeAccountAdmin(BaseAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")


@admin.register(Expense)
class ExpenseAdmin(BaseAdmin):
    list_display = ("account", "amount", "expense_against", "description", "date")
    search_fields = ("account", "amount", "expense_against", "description", "date")
    list_filter = ("account", "amount", "expense_against", "description", "date")
    autocomplete_fields = ("account", "expense_against")


@admin.register(Income)
class IncomeAdmin(BaseAdmin):
    list_display = ("account", "amount", "income_from", "description", "date")
    search_fields = ("account", "amount", "income_from", "description", "date")
    list_filter = ("account", "amount", "income_from", "description", "date")
    autocomplete_fields = ("account", "income_from")
