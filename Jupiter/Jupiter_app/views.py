from django.shortcuts import render, redirect
from .models import Paciente
from .forms import Cadastro, formLogin

def home(request):
    return render(request, './pagina_inicial.html')

def login(request):
    if request.method == 'POST':
        form = formLogin(request.POST)
        if form.is_valid():
            login = form.save()
            return render(request, 'homePaciente.html')
        else:
            return render(request, 'login.html')
    else:
        form = formLogin()
        return render(request, 'login.html', {'form': form})

def cadastrar(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            paciente = form.save()
            return render(request, 'sucessoCadastro.html')
        else:
            return render(request, 'falhaCadastro.html')
    else:
        form = Cadastro()
        return render(request, 'cadastrar.html', {'form': form})

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})
