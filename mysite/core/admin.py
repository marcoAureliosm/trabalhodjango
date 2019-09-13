from django.contrib import admin
from .models import *

class ContatoAdmim(admin.ModelAdmin):
     list_display = ('nome', 'email', 'telefone')
admin.site.register(Contato, ContatoAdmim)

class DespesaAdmin(admin.ModelAdmin):
     list_display = ('data_criacao','tipo_despesa', 'descricao','formas_pagamento','vencimento','quitado')
admin.site.register(Despesa, DespesaAdmin)

class ComprasAdmin(admin.ModelAdmin):
     list_display = ('nome','descricaoProduto','unidadeCompra', 'qtdPrevistoMes','preco','precoMaximo')
admin.site.register(Compras, ComprasAdmin)

class AnuncioAdmin(admin.ModelAdmin):
     list_display = ('cliente','textoTitulo', 'preco','TextoAnuncio','nomeContato','telefone','secao','tipoAnuncio')
admin.site.register(Anuncio, AnuncioAdmin)


# Register your models here.