from rest_framework import viewsets
from .models import PerfilMorador, Unidade
from .serializers import PerfilMoradorSerializer, UnidadeSerializer
from rest_framework.permissions import IsAuthenticated

class PerfilMoradorViewSet(viewsets.ModelViewSet):
    queryset = PerfilMorador.objects.all()
    serializer_class = PerfilMoradorSerializer
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar