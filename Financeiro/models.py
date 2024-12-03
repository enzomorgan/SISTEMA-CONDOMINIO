from django.db import models
from decimal import Decimal

class Unit(models.Model):
    number = models.CharField(max_length=10)
    block = models.CharField(max_length=10)
    owner_name = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Unit {self.number} - Block {self.block}"

class MonthlyFee(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='monthly_fees')
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def calculate_late_fee(self):
        if not self.paid and self.due_date < timezone.now().date():
            days_late = (timezone.now().date() - self.due_date).days
            self.late_fee = self.amount * Decimal('0.02') + (self.amount * Decimal('0.001') * days_late)
            self.save()

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('MAINTENANCE', 'Maintenance'),
        ('UTILITY', 'Utility'),
        ('STAFF', 'Staff'),
        ('INSURANCE', 'Insurance'),
        ('OTHER', 'Other')
    ]
    
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    paid = models.BooleanField(default=False)
    due_date = models.DateField()
    
    def __str__(self):
        return f"{self.description} - {self.amount}"

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('BANK_TRANSFER', 'Bank Transfer'),
        ('CREDIT_CARD', 'Credit Card'),
        ('PIX', 'PIX')
    ]
    
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='payments')
    monthly_fee = models.ForeignKey(MonthlyFee, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Payment {self.id} - Unit {self.unit.number}"