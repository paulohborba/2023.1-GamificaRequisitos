from django.db import models
from django.contrib.auth.models import User

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    pontos = models.PositiveIntegerField()
    data_entrega = models.DateField(blank=True)
    descricao_detalhada = models.TextField(blank=True)
    arquivos = models.FileField(upload_to='media/', blank=True)
    recursos = models.URLField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
