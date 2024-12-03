from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UnidadeViewSet,
    TaxaMensalViewSet,
    DespesaViewSet,
    PagamentoViewSet
)

router = DefaultRouter()
router.register(r'unidades', UnidadeViewSet)
router.register(r'taxas-mensais', TaxaMensalViewSet)
router.register(r'despesas', DespesaViewSet)
router.register(r'pagamentos', PagamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]