
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),

    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('homePaciente/', views.homePaciente, name='homePaciente'),
    path('sucessoCadastro/', views.sucessoCadastroView, name='sucessoCadastro'),
    path('falhaCadastro/', views.falhaCadastroView, name='falhaCadastro')
]
