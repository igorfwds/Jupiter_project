from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    endereco = models.TextField()
    complemento = models.TextField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    
    def _str_(self):
        return self.nome
