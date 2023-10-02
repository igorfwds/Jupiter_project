from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def paciente_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Autentica o usuário
            login(request, form.get_user())
            return redirect('homePaciente')
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
    return render(request, 'homePaciente.html', {'user_name': user_name})



def sucessoCadastroView(request):
    return render(request, 'sucessoCadastro.html')

def falhaCadastroView(request):
    return render(request, 'falhaCadastro.html')

