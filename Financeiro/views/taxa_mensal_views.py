from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from ..models import TaxaMensal
from ..serializers import TaxaMensalSerializer, PagamentoSerializer

class TaxaMensalViewSet(viewsets.ModelViewSet):
    queryset = TaxaMensal.objects.all()
    serializer_class = TaxaMensalSerializer
    
    @action(detail=True, methods=['post'])
    def registrar_pagamento(self, request, pk=None):
        taxa_mensal = self.get_object()
        
        if taxa_mensal.pago:
            return Response(
                {'erro': 'Esta taxa já foi paga'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        dados_pagamento = {
            'unidade': taxa_mensal.unidade.id,
            'taxa_mensal': taxa_mensal.id,
            'valor': request.data.get('valor', taxa_mensal.valor),
            'data_pagamento': request.data.get('data_pagamento', timezone.now().date()),
            'metodo_pagamento': request.data.get('metodo_pagamento'),
            'id_transacao': request.data.get('id_transacao')
        }
        
        serializer = PagamentoSerializer(data=dados_pagamento)
        if serializer.is_valid():
            serializer.save()
            taxa_mensal.pago = True
            taxa_mensal.data_pagamento = dados_pagamento['data_pagamento']
            taxa_mensal.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)