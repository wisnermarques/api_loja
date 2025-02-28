from rest_framework import serializers
from .models import Cliente, Produto, Venda, ItemDaVenda

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ItemDaVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDaVenda
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    itens = ItemDaVendaSerializer(many=True, read_only=True)

    class Meta:
        model = Venda
        fields = '__all__'