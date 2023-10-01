from django import forms
from .models import Paciente, Login


class Cadastro(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nome',
            'cpf', 
            'data_nascimento', 
            'endereco', 
            'complemento', 
            'email', 
            'celular'
        ]

class formLogin(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
            'cpf',
            'senha'
        ]