from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione campos adicionais do paciente, como nome, data de nascimento, etc.