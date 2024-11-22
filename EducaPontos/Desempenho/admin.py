from django.contrib import admin
from .models import Desempenho, Disciplina, Lancamento

# Registra os modelos para aparecer no painel de administração
admin.site.register(Desempenho)
admin.site.register(Disciplina)
admin.site.register(Lancamento)