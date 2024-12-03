"""
URL configuration for condominio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from casas.views import CasaViewSet
from rest_framework.routers import SimpleRouter
from .views import PerfilMoradorViewSet, UnidadeViewSet

router = SimpleRouter()
router.register("perfis", PerfilMoradorViewSet, basename="perfis")
router.register("unidades", UnidadeViewSet, basename="unidades")
router.register("casas", CasaViewSet, basename="casas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/moradores/', include('apps.moradores.urls')),
    #path('api/unidades/', include('apps.unidades.urls')),
    #path('api/financeiro/', include('apps.financeiro.urls')),
    path('api/usuarios/', include('apps.usuarios.urls')),
    path('api/casas/', include('apps.casas.urls')),
]
