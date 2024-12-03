def calcular_taxas_atrasadas():
    """Calcula multas para todas as taxas não pagas"""
    from ..models import TaxaMensal
    
    taxas_nao_pagas = TaxaMensal.objects.filter(pago=False)
    for taxa in taxas_nao_pagas:
        taxa.calcular_multa()