from django.db import models
from django.utils import timezone
from decimal import Decimal
from .unidade import Unidade

class TaxaMensal(models.Model):
    unidade = models.ForeignKey(
        Unidade, 
        on_delete=models.CASCADE, 
        related_name='taxas_mensais'
    )
    data_vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.BooleanField(default=False)
    data_pagamento = models.DateField(null=True, blank=True)
    multa = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def calcular_multa(self):
        if not self.pago and self.data_vencimento < timezone.now().date():
            dias_atraso = (timezone.now().date() - self.data_vencimento).days
            self.multa = self.valor * Decimal('0.02') + (self.valor * Decimal('0.001') * dias_atraso)
            self.save()
    
    def __str__(self):
        return f"Taxa {self.unidade} - Vencimento: {self.data_vencimento}"
    
    class Meta:
        verbose_name = 'Taxa Mensal'
        verbose_name_plural = 'Taxas Mensais'