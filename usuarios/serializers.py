from rest_framework import serializers
from .models import PerfilMorador, Unidade

class PerfilMoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilMorador
        fields = ['id', 'user', 'telefone', 'endereco', 'data_nascimento', 'unidade']

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = ['id', 'numero_unidade', 'morador', 'ocupada']