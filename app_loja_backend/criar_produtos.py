import os
import django

# Configure as configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_loja_backend.settings")
django.setup()

from loja.models import Produto

# Lista de produtos fictícios
produtos = [
    {"nome": "Camiseta Básica", "descricao": "Camiseta de algodão", "preco": 49.99, "estoque": 100},
    {"nome": "Calça Jeans", "descricao": "Calça jeans slim", "preco": 129.99, "estoque": 50},
    {"nome": "Tênis Esportivo", "descricao": "Tênis para corrida", "preco": 199.99, "estoque": 30},
    {"nome": "Mochila Escolar", "descricao": "Mochila resistente", "preco": 89.99, "estoque": 40},
    {"nome": "Relógio Digital", "descricao": "Relógio à prova d'água", "preco": 149.99, "estoque": 20},
    {"nome": "Fone de Ouvido", "descricao": "Fone com cancelamento de ruído", "preco": 299.99, "estoque": 25},
    {"nome": "Notebook", "descricao": "Notebook 8GB RAM", "preco": 2999.99, "estoque": 10},
    {"nome": "Smartphone", "descricao": "Smartphone 128GB", "preco": 1999.99, "estoque": 15},
    {"nome": "Tablet", "descricao": "Tablet 10 polegadas", "preco": 999.99, "estoque": 12},
    {"nome": "Cadeira Gamer", "descricao": "Cadeira ergonômica", "preco": 799.99, "estoque": 8},
    {"nome": "Mouse Gamer", "descricao": "Mouse com RGB", "preco": 199.99, "estoque": 30},
    {"nome": "Teclado Mecânico", "descricao": "Teclado com switches azuis", "preco": 299.99, "estoque": 20},
    {"nome": "Monitor 24''", "descricao": "Monitor Full HD", "preco": 899.99, "estoque": 10},
    {"nome": "Impressora", "descricao": "Impressora multifuncional", "preco": 499.99, "estoque": 5},
    {"nome": "Câmera DSLR", "descricao": "Câmera profissional", "preco": 3999.99, "estoque": 3},
    {"nome": "Drone", "descricao": "Drone com câmera 4K", "preco": 1999.99, "estoque": 7},
    {"nome": "Console de Videogame", "descricao": "Console última geração", "preco": 2499.99, "estoque": 6},
    {"nome": "Smartwatch", "descricao": "Smartwatch com GPS", "preco": 599.99, "estoque": 15},
    {"nome": "Caixa de Som", "descricao": "Caixa de som Bluetooth", "preco": 199.99, "estoque": 20},
    {"nome": "Headset", "descricao": "Headset com microfone", "preco": 299.99, "estoque": 18},
]

# Cria os produtos no banco de dados
for produto in produtos:
    novo_produto = Produto(
        nome=produto["nome"],
        descricao=produto["descricao"],
        preco=produto["preco"],
        estoque=produto["estoque"],
    )
    novo_produto.save()

print("20 produtos cadastrados com sucesso!")