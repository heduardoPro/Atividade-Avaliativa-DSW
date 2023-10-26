from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def Cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'cadastrar_alunos.html', {'form': form})

def Detalhar_aluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    return render(request, 'detalhar_aluno.html', {'aluno': aluno})

def Listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})

def Atualizar_aluno(request, pk):
    aluno = Aluno.objects.all()
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_aluno')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'atualizar_aluno.html', {'form': form})

def Deletar_aluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    aluno.delete()
    return redirect('lista_aluno')

