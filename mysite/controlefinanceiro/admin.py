from django.contrib import admin
from .models import Categoria, Transacao, ContasPagar, ContasReceber

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Transacao)
admin.site.register(ContasPagar)
admin.site.register(ContasReceber)