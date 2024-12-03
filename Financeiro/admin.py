from django.contrib import admin
from .models import Unidade, TaxaMensal, Despesa, Pagamento

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('numero', 'bloco', 'proprietario', 'area')
    search_fields = ('numero', 'bloco', 'proprietario')

@admin.register(TaxaMensal)
class TaxaMensalAdmin(admin.ModelAdmin):
    list_display = ('unidade', 'data_vencimento', 'valor', 'pago', 'data_pagamento', 'multa')
    list_filter = ('pago', 'data_vencimento')
    search_fields = ('unidade__numero', 'unidade__proprietario')

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'categoria', 'pago')
    list_filter = ('categoria', 'pago', 'data')
    search_fields = ('descricao',)

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('unidade', 'taxa_mensal', 'valor', 'data_pagamento', 'metodo_pagamento')
    list_filter = ('metodo_pagamento', 'data_pagamento')
    search_fields = ('unidade__numero', 'id_transacao')