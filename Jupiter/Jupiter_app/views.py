from django.shortcuts import render, redirect
from .models import Paciente
from .forms import Cadastro, formLogin
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, './pagina_inicial.html')


def login(request):
    if request.method == 'POST':
        form = formLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['senha']
            user = authenticate(request, username=email, password=password)  # Use o email como username
            if user is not None:
                login(request, user)
                print("User is authenticated")
                return redirect('homePaciente')
            else:
                print("User isn't authenticated")
        else:
            print("Form is not valid")
    else:
        form = formLogin()
    return render(request, 'login.html', {'form': form})


def cadastrar(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            try:
                paciente = form.save()
                return redirect( 'sucessoCadastro')
            except Exception as e:
                print("Exceção ao tentar salvar o paciente:", str(e))
                return redirect('falhaCadastro')
        
            
        else:
            print("Erro ao cadastrar:", form.errors)
            return redirect( 'falhaCadastro')
    else:
        form = Cadastro()
        return render(request, 'cadastrar.html', {'form': form})

def homePaciente(request):

    # Verifique se o usuário está autenticado
    if request.user.is_authenticated:
        # Acesse o nome do usuário logado
        user_name = request.user.username  # Se o campo for 'username'
        # Ou use user_name = request.user.nome se o campo for 'nome'
    else:
        # Usuário não autenticado, defina um valor padrão
        user_name = "Visitante"

    # Renderize a página HTML da home do paciente com o nome do usuário
    return redirect( 'homePaciente.html', {'user_name': user_name})



def sucessoCadastroView(request):
    return render(request, 'sucessoCadastro.html')

def falhaCadastroView(request):
    return render(request, 'falhaCadastro.html')

