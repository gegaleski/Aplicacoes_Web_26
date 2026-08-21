from django.contrib import admin
from .models import (
    Produto,
    Categoria,
    Cliente,
    Pedido,
    ItemPedido
    )
# Register your models here.


# Registrando categoria admin

@admin.register(Categoria)

class CategoriaAdmin(admin.ModelAdmin):

    list_display = ["id", "nome"]

    #filtro searchField
    search_fields = ["nome"]

    
@admin.register(Produto)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "quantidade", "preco", "created_at"]
    search_fields = ["nome",]
    list_filter = ["categoria"]


# Cliente

@admin.register(Cliente)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "email", "telefone"]
    search_fields = ["nome", "email"]


# Item do pedido 

class ItemPedidoInline(admin.TabularInline):
    # TabularInline para poder colocar um pedido embaixo do outro
    model = ItemPedido
    extra = 1
    fields = [
        "produto",
        "quantidade",
        "preco_unit"
    ]

# Pedido 

class PedidoAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "cliente",
        "data_pedido",
        "status",
        "valor_total"
    ]

    list_filter = [
        "status",
        "data_pedido"
    ]

    search_fields = [
        "cliente_nome",
        "cliente_email"
    ]

    inlines = [
        ItemPedidoInline
    ]

    def valor_total(self, obj):
        return obj.total()

    valor_total.short_description = "Total"


# ItemPedido

@admin.register(ItemPedido)

class ItemPedidoAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "pedido",
        "produto",
        "quantidade",
        "preco_unit",
        "valor_subtotal"
    ]

    search_fields = [
        "produto_nome",
        "pedido_cliente_nome"
    ]

    def valor_subtotal(self, obj):
        return obj.subtotal()

    valor_subtotal.short_description = "Subtotal"
