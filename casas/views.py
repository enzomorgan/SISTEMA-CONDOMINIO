from rest_framework import viewsets
from .models import Casa
from .serializers import CasaSerializer
from rest_framework.permissions import IsAuthenticated

class CasaViewSet(viewsets.ModelViewSet):
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar