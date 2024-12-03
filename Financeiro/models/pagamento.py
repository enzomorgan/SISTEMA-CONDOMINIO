from django.db import models
from .unidade import Unidade
from .taxa_mensal import TaxaMensal

class Pagamento(models.Model):
    METODOS_PAGAMENTO = [
        ('DINHEIRO', 'Dinheiro'),
        ('TRANSFERENCIA', 'Transferência Bancária'),
        ('CARTAO', 'Cartão de Crédito'),
        ('PIX', 'PIX')
    ]
    
    unidade = models.ForeignKey(
        Unidade, 
        on_delete=models.CASCADE, 
        related_name='pagamentos'
    )
    taxa_mensal = models.ForeignKey(
        TaxaMensal, 
        on_delete=models.CASCADE, 
        related_name='pagamentos'
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    metodo_pagamento = models.CharField(max_length=20, choices=METODOS_PAGAMENTO)
    id_transacao = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Pagamento {self.id} - Unidade {self.unidade.numero}"
    
    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'