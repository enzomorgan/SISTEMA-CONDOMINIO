from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from ..models import Pagamento
from ..serializers import PagamentoSerializer

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    
    @action(detail=False, methods=['get'])
    def resumo_mensal(self, request):
        resumo = Pagamento.objects.annotate(
            mes=TruncMonth('data_pagamento')
        ).values('mes').annotate(
            total=Sum('valor')
        ).order_by('mes')
        return Response(resumo)