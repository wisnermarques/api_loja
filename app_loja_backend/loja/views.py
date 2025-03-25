from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions
from .models import Cliente, Produto, Venda, ItemDaVenda
from .serializers import ClienteSerializer, ProdutoSerializer, RegistroSerializer, VendaSerializer, ItemDaVendaSerializer
from rest_framework import serializers
from .models import Cliente


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

# Paginação para as vendas
class VendaPagination(PageNumberPagination):
    page_size = 10  # Define 10 vendas por página
    page_size_query_param = 'page_size'  # Permite definir um tamanho diferente via query param
    max_page_size = 100  # Limita o máximo de vendas por página

# View que retorna as vendas de um cliente específico
class VendasPorClienteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, cliente_id, format=None):
        # Filtra as vendas do cliente e ordena pela data em ordem decrescente
        vendas = Venda.objects.filter(cliente_id=cliente_id).order_by('-data_venda')

        # Aplica a paginação
        paginator = VendaPagination()
        paginated_vendas = paginator.paginate_queryset(vendas, request)
        if paginated_vendas is not None:
            serializer = VendaSerializer(paginated_vendas, many=True)
            return paginator.get_paginated_response(serializer.data)

        # Caso não haja paginação
        serializer = VendaSerializer(vendas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClientePorUsernameView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username, format=None):
        try:
            user = User.objects.get(username=username)
            cliente = Cliente.objects.get(user=user)
            serializer = ClienteSerializer(cliente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'erro': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Cliente.DoesNotExist:
            return Response({'erro': 'Cliente não encontrado para este usuário'}, status=status.HTTP_404_NOT_FOUND)
        
class RegistroView(APIView):
    permission_classes = [AllowAny]  # Permitir acesso a qualquer um

    @method_decorator(csrf_exempt)  # Desativa a proteção CSRF
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensagem": "Cliente cadastrado com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)