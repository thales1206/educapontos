from django.db import models
from django.contrib.auth.models import User 


class Instituicao(models.Model):
    cnpj = models.CharField(max_length=15, unique=True)
    nome = models.CharField(max_length=200) 
    def __str__(self):
        return self.nome 
    
class Funcionario(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    codigo = models.CharField(max_length=200, unique=True)
    cargo = models.CharField( max_length=20, choices=[('Professor', 'Professor'), ('Coordenador', 'Coordenador'), ('Outro', 'Outro')], )
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='funcionarios')
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.cargo}"