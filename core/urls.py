from django.urls import path
from . import views

urlpatterns = [
    path('', views.Listar_alunos, name='Listar_alunos'),
    path('cadastrar_aluno/', views.Cadastrar_aluno, name='Cadastrar_aluno'),
    path('detalhar_aluno/<int:aluno_id>', views.Detalhar_aluno, name='Detalhar_aluno'),
    path('atualizar_aluno/<int:aluno_id>', views.Atualizar_aluno, name='Atualizar_aluno'),
    path('deletar_aluno/<int:aluno_id>', views.Deletar_aluno, name='Deletar_aluno'),
]
