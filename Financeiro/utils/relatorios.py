def gerar_relatorio_financeiro(data_inicio, data_fim):
    """Gera relatório financeiro para um período específico"""
    from django.db.models import Sum
    from ..models import TaxaMensal, Despesa
    
    receitas = TaxaMensal.objects.filter(
        pago=True,
        data_pagamento__range=[data_inicio, data_fim]
    ).aggregate(total=Sum('valor'))['total'] or 0
    
    despesas = Despesa.objects.filter(
        data__range=[data_inicio, data_fim]
    ).aggregate(total=Sum('valor'))['total'] or 0
    
    return {
        'periodo_inicio': data_inicio,
        'periodo_fim': data_fim,
        'total_receitas': receitas,
        'total_despesas': despesas,
        'saldo': receitas - despesas
    }