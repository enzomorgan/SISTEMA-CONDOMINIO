from rest_framework import serializers
from .models import Unit, MonthlyFee, Expense, Payment

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class MonthlyFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyFee
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['unit_info'] = str(instance.unit)
        return representation

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['unit_info'] = str(instance.unit)
        return representation