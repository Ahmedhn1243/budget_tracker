from django.db import models
from django.utils import timezone

class Budget(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()

    def __str__(self):
        return f"Budget for {self.month.strftime('%B %Y')} - {self.amount}"

class Expense(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.description} - {self.amount}"
