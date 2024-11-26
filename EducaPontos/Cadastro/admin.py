from django.contrib import admin
from .models import Instituicao
from .models import Funcionario


# Registra os modelos para aparecer no painel de administração
admin.site.register(Instituicao)
admin.site.register(Funcionario)
# Register your models here.
