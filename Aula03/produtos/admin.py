from django.contrib import admin

# Register your models here.

@admin.register(Produto)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "quantidade", "preco", "created_at")
    search_fields = ("nome",)
