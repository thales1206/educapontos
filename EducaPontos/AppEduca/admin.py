from django.contrib import admin
from .models import Aluno
from .models import Turma


# Registra os modelos para aparecer no painel de administração
admin.site.register(Aluno)
admin.site.register(Turma)

