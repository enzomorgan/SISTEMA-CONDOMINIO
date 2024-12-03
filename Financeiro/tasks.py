from celery import shared_task
from decimal import Decimal
from .utils import gerar_taxas_mensais, calcular_taxas_atrasadas

@shared_task
def tarefa_gerar_taxas_mensais():
    """Tarefa para gerar automaticamente as taxas mensais"""
    valor_base = Decimal('500.00')  # Valor base para taxas mensais
    gerar_taxas_mensais(valor_base)

@shared_task
def tarefa_calcular_multas():
    """Tarefa para calcular multas diariamente"""
    calcular_taxas_atrasadas()