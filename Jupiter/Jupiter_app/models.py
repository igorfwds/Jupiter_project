from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False,default='none')
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False,default='none')
    data_nascimento = models.DateField(blank=False,default='none')
    endereco = models.CharField(max_length=100, null=False, blank=False,default='none')
    complemento = models.CharField(max_length=100,default='Sem Complemento')
    email = models.EmailField(max_length=254, blank=False, null=False,default='none')
    celular = models.CharField(max_length=14, blank=False, null=False,default='none' )
    senha = models.CharField(max_length=100,blank=False,null=False,default='none')
    rg = models.CharField(max_length=12, unique=True,blank=False,null=False,default='none')
    cep = models.CharField(max_length=9,blank=False,null=False,default='none')
    tipo_sanguineo = models.CharField(max_length=5, blank=True, null=True,default='Nada Consta')
    alergias = models.TextField(blank=True, null=True,default='Nada Consta')
    remedios = models.TextField(blank=True, null=True,default='Nada Consta')
    peso = models.FloatField(blank=True, null=True,default=0.0)
    altura = models.FloatField(blank=True, null=True,default=0.0)
    
    def __str__(self):
        return self.nome

class Login(models.Model):
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50, null=False, blank=False)

