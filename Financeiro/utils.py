from datetime import datetime
from dateutil.relativedelta import relativedelta
from .models import MonthlyFee, Unit

def generate_monthly_fees(base_amount):
    """Generate monthly fees for all units"""
    units = Unit.objects.all()
    next_month = datetime.now().date() + relativedelta(months=1)
    next_month = next_month.replace(day=1)
    
    fees_created = []
    for unit in units:
        # Calculate fee based on unit area
        adjusted_amount = base_amount * (unit.area / 100)  # Example calculation
        
        fee = MonthlyFee.objects.create(
            unit=unit,
            due_date=next_month,
            amount=adjusted_amount
        )
        fees_created.append(fee)
    
    return fees_created

def calculate_late_fees():
    """Calculate late fees for all unpaid monthly fees"""
    unpaid_fees = MonthlyFee.objects.filter(paid=False)
    for fee in unpaid_fees:
        fee.calculate_late_fee()

def generate_financial_report(start_date, end_date):
    """Generate a financial report for a specific period"""
    from django.db.models import Sum
    
    income = MonthlyFee.objects.filter(
        paid=True,
        paid_date__range=[start_date, end_date]
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    expenses = Expense.objects.filter(
        date__range=[start_date, end_date]
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    return {
        'period_start': start_date,
        'period_end': end_date,
        'total_income': income,
        'total_expenses': expenses,
        'balance': income - expenses
    }