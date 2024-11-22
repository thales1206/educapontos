from django.db import models
from AppEduca.models import Aluno

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Lancamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='lancamentos')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='lancamentos')
    media = models.DecimalField(max_digits=5, decimal_places=2)
    frequencia = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Lançamento de {self.aluno} - {self.disciplina}"

class Desempenho(models.Model):
    aluno = models.ForeignKey(Aluno,  # Referência ao Aluno
        on_delete=models.CASCADE, related_name='desempenhos')
    
    pontos = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Desempenho de {self.aluno}: {self.pontos} pontos"
