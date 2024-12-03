from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Unidade, Pagamento
from ..serializers import UnidadeSerializer, PagamentoSerializer

class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer
    
    @action(detail=True, methods=['get'])
    def historico_pagamentos(self, request, pk=None):
        unidade = self.get_object()
        pagamentos = Pagamento.objects.filter(unidade=unidade).order_by('-data_pagamento')
        serializer = PagamentoSerializer(pagamentos, many=True)
        return Response(serializer.data)