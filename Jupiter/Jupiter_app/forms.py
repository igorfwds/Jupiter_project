from django import forms
from .models import Paciente, Login


class Cadastro(forms.ModelForm):
    nome = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=14)
    data_nascimento = forms.DateField()
    endereco = forms.CharField(max_length=100)
    complemento = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    celular = forms.CharField(max_length=14 )
    senha = forms.CharField(max_length=100)
    rg = forms.CharField(max_length=12)
    cep = forms.CharField(max_length=9,)
    tipo_sanguineo = forms.CharField(max_length=5)
    alergias = forms.CharField(widget=forms.Textarea)
    remedios = forms.CharField(widget=forms.Textarea)
    peso = forms.FloatField()
    altura = forms.FloatField()

    class Meta:
        model = Paciente
        fields = [
            'nome',
            'cpf', 
            'data_nascimento', 
            'endereco', 
            'complemento', 
            'email', 
            'celular',
            'senha',
            'rg',
            'cep',
            'tipo_sanguineo',
            'alergias',
            'remedios',
            'peso',
            'altura'
        ]

class formLogin(forms.ModelForm):
    email = forms.EmailField(max_length=254 )
    senha = forms.CharField(max_length=100)
    
    nome = forms.CharField(max_length=100 )
    cpf = forms.CharField(max_length=14 )
    data_nascimento = forms.DateField()
    endereco = forms.CharField(max_length=100 )
    complemento = forms.CharField(max_length=100)
    celular = forms.CharField(max_length=14)
    rg = forms.CharField(max_length=12)
    cep = forms.CharField(max_length=9)
    tipo_sanguineo = forms.CharField(max_length=5 )
    alergias = forms.CharField(widget=forms.Textarea)
    remedios = forms.CharField(widget=forms.Textarea)
    peso = forms.FloatField()
    altura = forms.FloatField()

    class Meta:
        model = Login
        fields = [
            'email',
            'senha'
        ]


