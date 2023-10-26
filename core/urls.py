from django.urls import path
from . import views

urlpatterns = [
    path('', views.Listar_alunos, name='Listar_alunos'),
    path('cadastrar_aluno/', views.Cadastrar_aluno, name='Cadastrar_aluno'),
    path('<int:pk>/atualizar_aluno/', views.Atualizar_aluno, name='Atualizar_aluno'),
    path('<int:pk>/detalhar_aluno/', views.Detalhar_aluno, name='Detalhar_alunos'),
    path('<int:pk>/deletar_aluno/', views.Deletar_aluno, name='Deletar_aluno'),
]
