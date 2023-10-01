from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False,default='XXX.XXX.XXX-XX')
    data_nascimento = models.DateField(blank=False)
    endereco = models.CharField(max_length=100, null=False, blank=False)
    complemento = models.CharField(max_length=100,default='Sem Complemento')
    email = models.EmailField(max_length=254, blank=False, null=False)
    celular = models.CharField(max_length=14, blank=False, null=False, default='XX XXXX-XXXX')

    
    def __str__(self):
        return self.nome

class Login(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50, null=False, blank=False)
