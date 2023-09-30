from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def login(request):
    return render(request, 'login.html')

def cadastrar(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'cadastrar.html', {'form': form})

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})
