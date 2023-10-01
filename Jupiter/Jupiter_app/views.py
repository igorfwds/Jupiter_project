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
            print("User is authenticated")
            return redirect('homePaciente.html')
        else:
            print("User isn't authenticated")
            return render(request, 'login.html')
    else:
        form = formLogin()
        return render(request, 'login.html', {'form': form})

def cadastrar(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            paciente = form.save()
            print("deu")
            return redirect( 'sucessoCadastro')
        else:
            print("n deu")
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

