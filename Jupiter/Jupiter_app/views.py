from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CadastroForm
from .models import Exame, Receituario  # Importe o modelo Exame

def paciente_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']  # Pega o email do campo username
            senha = form.cleaned_data['password']
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                return redirect('homePaciente')
            else:
                print("Usuário ou senha incorreto!")
                messages.error(request, "Usuário ou senha incorreto!")
        else:
            print("Usuário ou senha incorreto!")
            messages.error(request, "Usuário ou senha incorreto!")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})





def home(request):
    return render(request, './pagina_inicial.html')


def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            try:
                # Crie um usuário User separado
                user = User.objects.create_user(username=form.cleaned_data['email'], password=form.cleaned_data['senha'])

                # Crie uma instância do paciente a partir do formulário
                paciente = form.save(commit=False)

                # Associe o usuário ao paciente
                paciente.user = user
                
                # Salve o paciente no banco de dados
                paciente.save()

                return redirect('sucessoCadastro')
            except Exception as e:
                print("Exceção ao tentar salvar o paciente:", str(e))
                return redirect('falhaCadastro')
        else:
            print("Erro ao cadastrar:", form.errors)
            return redirect('falhaCadastro')
    else:
        form = CadastroForm()
        return render(request, 'cadastrar.html', {'form': form})


def homePaciente(request):
    return render(request, 'homePaciente.html')



def sucessoCadastroView(request):
    return render(request, 'sucessoCadastro.html')

def falhaCadastroView(request):
    return render(request, 'falhaCadastro.html')

def exibir_exames(request):
    exames = Exame.objects.all()

    return render(request, 'exames.html', {'exames': exames})

def exibir_receituarios(request):
    receitas = Receituario.objects.all()

    return render(request, 'receituarios.html', {'receitas': receitas})
