from django.db import models

# Create your models here.
#Sempre que eu criar ou modificar modelos, eu tenho que fazer uma migração
# python manage.py makemigrations
# python manage.py migrate
class Categoria(models.Model):
    tipo_transacao = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa')
    ]
    idCategoria = models.BigAutoField(primary_key=True)
    nomeGrupo = models.CharField(max_length=100)
    nomeCategoria = models.CharField(max_length=100)
    nomeDescricao = models.CharField(max_length=100)
    tipoTransacao = models.CharField(max_length=50, choices=tipo_transacao)
    isActive = models.BooleanField(default=True)
    creationDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

class Transacao(models.Model):
    idTransacao = models.BigAutoField(primary_key=True)
    valorTransacao = models.DecimalField(max_digits=10, decimal_places=2)
    descricaoTransacao = models.CharField(max_length=100)
    dataTransacao = models.DateField()
    idCategoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    dataCriacao = models.DateField(auto_now_add=True)
    dataAtualizacao = models.DateField(auto_now=True)

class ContasReceber(models.Model):
    tipos_status = [
        ('aguardando', 'Aguardando'),
        ('vencendo', 'Na Data'),
        ('recebido', 'Recebido')
    ]
    idReceber = models.BigAutoField(primary_key=True)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    valorReceber = models.DecimalField(max_digits=10, decimal_places=2)
    dataRecebimentoPrevista = models.DateField()
    dataRecebimentoEfetiva = models.DateField()
    statusRecebimento = models.CharField(max_length=50, choices=tipos_status)
    observacaoRecebimento = models.TextField()

class ContasPagar(models.Model):
    status_pagamentos = [
        ('antes', 'A pagar'),
        ('vencendo', 'Vencendo'),
        ('pago', 'Pago')
    ]
    idPagamento = models.BigAutoField(primary_key=True)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    valorPagar = models.DecimalField(max_digits=10, decimal_places=2)
    dataPagamentoPrevisto = models.DateField()
    dataPagamentoRealizado = models.DateField()
    statusPagamento = models.CharField(max_length=50, choices=status_pagamentos)
