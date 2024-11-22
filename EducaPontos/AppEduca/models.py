from django.db import models
from django.contrib.auth.models import User
from Cadastro.models import Instituicao

class Turma(models.Model):
    nome = models.CharField(max_length=200)
    
def __str__(self):
    return self.nome

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=200, unique=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos')
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='alunos')
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.turma.nome}"