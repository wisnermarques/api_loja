from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from .models import Cliente, Produto, Venda, ItemDaVenda
from .serializers import ClienteSerializer, ProdutoSerializer, VendaSerializer, ItemDaVendaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProdutoPagination(PageNumberPagination):
    page_size = 10  # Define 10 produtos por página
    page_size_query_param = 'page_size'  # Permite definir um tamanho diferente via query param
    max_page_size = 100  # Limita o máximo de produtos por página

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    pagination_class = ProdutoPagination  # Adiciona paginação personalizada

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ItemDaVendaViewSet(viewsets.ModelViewSet):
    queryset = ItemDaVenda.objects.all()
    serializer_class = ItemDaVendaSerializer
    permission_classes = [permissions.IsAuthenticated]