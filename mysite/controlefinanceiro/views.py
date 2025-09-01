from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Categoria, Transacao, ContasPagar, ContasReceber
from .serializers import CategoriaSerializer, TransacaoSerializer, ContasPagarSerializer, ContasReceberSerializer

# Create your views here.
def teste_template(request):
    return render(request, 'base.html')

def teste_categorias(request):
    return render(request, 'categorias.html')

class CategoriasViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Categoria.objects.all()
        serializer = CategoriaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        categoria = get_object_or_404(Categoria, pk=pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def update(self, request, pk=None):
        categoria = get_object_or_404(Categoria, pk=pk)
        serializer = CategoriaSerializer(categoria, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk=None):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return Response(status=204)