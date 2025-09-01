from rest_framework import serializers
from .models import Categoria, Transacao, ContasPagar, ContasReceber

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['idCategoria', 'nomeGrupo', 'nomeCategoria', 'nomeDescricao', 'tipoTransacao', 'isActive', 'creationDate', 'updatedDate']

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['idTransacao', 'valorTransacao', 'descricaoTransacao', 'dataTransacao', 'idCategoria', 'dataCriacao']

class ContasReceberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContasReceber
        fields = ['idReceber', 'idCategoria', 'valorReceber', 'dataRecebimentoPrevista', 'dataRecebimentoEfetiva', 'statusRecebimento', 'observacaoRecebimento']

class ContasPagarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContasPagar
        fields = ['idPagamento', 'idCategoria', 'valorPagar', 'dataPagamentoPrevisto', 'dataPagamentoRealizado', 'statusPagamento']
