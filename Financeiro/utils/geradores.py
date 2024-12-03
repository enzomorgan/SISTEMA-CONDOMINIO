from datetime import datetime
from dateutil.relativedelta import relativedelta
from ..models import TaxaMensal, Unidade

def gerar_taxas_mensais(valor_base):
    """Gera taxas mensais para todas as unidades"""
    unidades = Unidade.objects.all()
    proximo_mes = datetime.now().date() + relativedelta(months=1)
    proximo_mes = proximo_mes.replace(day=1)
    
    taxas_criadas = []
    for unidade in unidades:
        # Calcula taxa baseada na área da unidade
        valor_ajustado = valor_base * (unidade.area / 100)
        
        taxa = TaxaMensal.objects.create(
            unidade=unidade,
            data_vencimento=proximo_mes,
            valor=valor_ajustado
        )
        taxas_criadas.append(taxa)
    
    return taxas_criadas