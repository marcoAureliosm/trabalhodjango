from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    endereço = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()

class Despesa(models.Model):
    data_criacao= models.DateField()
    tipo_despesa = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    Boleto = 'Boleto'
    Credito = 'Credito'
    Debito = 'Debito'
    formas_pagamento = (
        (Boleto, 'Boleto'),
        (Credito, 'Credito'),
        (Debito, 'Debito'),
    )
    formas_pagamento = models.CharField(
        max_length=2,
        choices=formas_pagamento,
        default=Boleto,
    )

    def is_upperclass(self):
        return self.formas_pagamento in (self.Boleto, self.Credito, self.Debito)

    vencimento = models.DateField()
    quitado = models.BooleanField()

class Compras(models.Model):
    nome = models.CharField(max_length=50)
    descricaoProduto = models.CharField(max_length=50)
    unidadeCompra = models.CharField(max_length=50)
    qtdPrevistoMes = models.DecimalField( max_digits=10, decimal_places=2)
    preco = models.DecimalField( max_digits=1000, decimal_places=2)
    precoMaximo = models.DecimalField(max_digits=1000, decimal_places=2)

class Anuncio(models.Model):
    cliente = models.CharField(max_length=50)
    textoTitulo = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=1000, decimal_places=2)
    TextoAnuncio = models.CharField(max_length=50)
    nomeContato = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    secao = models.CharField(max_length=50)
    tipoAnuncio = models.CharField(max_length=50)





# Create your models here.

def __str__(self):
    return self.nome
