from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = 'nome', 'uf',
    ordering = 'id',

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'endereco', 'email', 'data_nascimento',
    ordering = '-id',

@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = 'nome',
    ordering = '-id',
