from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientePorUsernameView, ClienteViewSet, ProdutoViewSet, VendaViewSet, ItemDaVendaViewSet, VendasPorClienteView, RegistroView

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'vendas', VendaViewSet)
router.register(r'itens-da-venda', ItemDaVendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vendas/cliente/<int:cliente_id>/', VendasPorClienteView.as_view(), name='vendas-por-cliente'),  # Adiciona a URL para as vendas por cliente
    path('clientes/username/<str:username>/', ClientePorUsernameView.as_view(), name='cliente-por-username'),
    path('registrar/', RegistroView.as_view(), name='registro'),
]