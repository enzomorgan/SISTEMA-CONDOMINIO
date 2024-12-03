from rest_framework import serializers
from ..models import Pagamento

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['info_unidade'] = str(instance.unidade)
        return representation