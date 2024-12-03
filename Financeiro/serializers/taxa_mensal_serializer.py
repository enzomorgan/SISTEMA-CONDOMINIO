from rest_framework import serializers
from ..models import TaxaMensal

class TaxaMensalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxaMensal
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['info_unidade'] = str(instance.unidade)
        return representation