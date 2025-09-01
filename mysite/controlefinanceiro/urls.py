from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriasViewSet, teste_categorias

router = DefaultRouter()
router.register(r'categorias', CategoriasViewSet, basename='categorias')

urlpatterns = [
    path('', include(router.urls)),
    path('categorias-page/', teste_categorias, name='categorias-page')
]