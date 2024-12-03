from rest_framework import serializers
from .models import Casa

class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = ['id', 'numero_casa', 'morador', 'ocupada']