from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=200, blank=True)
    endereco = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    data_nascimento = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome