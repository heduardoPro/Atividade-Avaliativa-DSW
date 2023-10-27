from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def Cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Listar_alunos'))
    else:
        form = AlunoForm()
    return render(request, 'cadastrar_alunos.html', {'form': form})

def Detalhar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    return render(request, 'detalhar_aluno.html', {'aluno': aluno})

def Listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})

def Atualizar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, pk=aluno_id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(Listar_alunos))
        else:
            return render(request, 'editar_aluno.html', {'form': form})
        
    else:
        form = AlunoForm(instance=aluno)
        return render(request, 'editar_aluno.html', {'form': form})


def Deletar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(pk=aluno_id)
    aluno.delete()
    return HttpResponseRedirect(reverse(Listar_alunos))