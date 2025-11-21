from core.base import BaseModel
from django.db import models


class ExpenseAccount(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class Expense(BaseModel):
    account = models.ForeignKey(ExpenseAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_against = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return str(self.account)


class IncomeAccount(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class Income(BaseModel):
    account = models.ForeignKey(IncomeAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    income_from = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return str(self.account)
