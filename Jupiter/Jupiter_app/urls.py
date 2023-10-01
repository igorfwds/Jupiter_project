from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),

    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
]
