from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Unit, MonthlyFee, Expense, Payment
from .serializers import UnitSerializer, MonthlyFeeSerializer, ExpenseSerializer, PaymentSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    
    @action(detail=True, methods=['get'])
    def payment_history(self, request, pk=None):
        unit = self.get_object()
        payments = Payment.objects.filter(unit=unit).order_by('-payment_date')
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

class MonthlyFeeViewSet(viewsets.ModelViewSet):
    queryset = MonthlyFee.objects.all()
    serializer_class = MonthlyFeeSerializer
    
    @action(detail=True, methods=['post'])
    def register_payment(self, request, pk=None):
        monthly_fee = self.get_object()
        
        if monthly_fee.paid:
            return Response(
                {'error': 'This fee has already been paid'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        payment_data = {
            'unit': monthly_fee.unit.id,
            'monthly_fee': monthly_fee.id,
            'amount': request.data.get('amount', monthly_fee.amount),
            'payment_date': request.data.get('payment_date', timezone.now().date()),
            'payment_method': request.data.get('payment_method'),
            'transaction_id': request.data.get('transaction_id')
        }
        
        serializer = PaymentSerializer(data=payment_data)
        if serializer.is_valid():
            serializer.save()
            monthly_fee.paid = True
            monthly_fee.paid_date = payment_data['payment_date']
            monthly_fee.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    @action(detail=False, methods=['get'])
    def summary_by_category(self, request):
        from django.db.models import Sum
        summary = Expense.objects.values('category').annotate(
            total=Sum('amount')
        ).order_by('category')
        return Response(summary)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    @action(detail=False, methods=['get'])
    def monthly_summary(self, request):
        from django.db.models import Sum
        from django.db.models.functions import TruncMonth
        
        summary = Payment.objects.annotate(
            month=TruncMonth('payment_date')
        ).values('month').annotate(
            total=Sum('amount')
        ).order_by('month')
        return Response(summary)