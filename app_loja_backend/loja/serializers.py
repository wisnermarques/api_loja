from rest_framework import serializers
from .models import Cliente, Produto, Venda, ItemDaVenda
from django.contrib.auth.models import User

class ClienteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Cliente
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ItemDaVendaSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = ItemDaVenda
        fields = ['id', 'produto', 'quantidade', 'preco_unitario', 'product_name']

    def get_product_name(self, obj):
        return obj.produto.nome if obj.produto else None


class VendaSerializer(serializers.ModelSerializer):
    itens = ItemDaVendaSerializer(many=True)  # Permite receber itens no POST

    class Meta:
        model = Venda
        fields = '__all__'

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')  # Remove os itens do dict principal
        venda = Venda.objects.create(**validated_data)  # Cria a venda

        # Criar os itens associados à venda
        for item_data in itens_data:
            ItemDaVenda.objects.create(venda=venda, **item_data)

        return venda

    def to_representation(self, instance):
        """Retorna os itens corretamente na resposta"""
        response = super().to_representation(instance)
        response['itens'] = ItemDaVendaSerializer(instance.itens.all(), many=True).data
        return response
    

class RegistroSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Cliente
        fields = ['username', 'password', 'telefone', 'endereco']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        # Criar o usuário
        user = User.objects.create_user(username=username, password=password)

        # Criar o cliente associado ao usuário
        cliente = Cliente.objects.create(user=user, **validated_data)

        return cliente
