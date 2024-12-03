from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from ..models import Despesa
from ..serializers import DespesaSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    
    @action(detail=False, methods=['get'])
    def resumo_por_categoria(self, request):
        resumo = Despesa.objects.values('categoria').annotate(
            total=Sum('valor')
        ).order_by('categoria')
        return Response(resumo)