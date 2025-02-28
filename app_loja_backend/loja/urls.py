from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ProdutoViewSet, VendaViewSet, ItemDaVendaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'itens-da-venda', ItemDaVendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]