from django.shortcuts import render, redirect

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def login(request):
    # Implemente a lógica de login aqui
    return render(request, 'login.html')

def cadastrar(request):
    # Implemente a lógica de cadastro aqui
    return render(request, 'cadastrar.html')