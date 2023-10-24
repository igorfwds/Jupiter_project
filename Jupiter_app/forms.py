from django import forms
from .models import Paciente, Exame, Receituario
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate  



class LoginForm(AuthenticationForm):
    email = forms.EmailField(required=True)
    senha = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        senha = cleaned_data.get('senha')

        if email is not None and senha:
            self.user_cache = authenticate(self.request, username=email, password=senha)
            if self.user_cache is None:
                raise forms.ValidationError('Usuário ou senha incorreto.')
        return self.cleaned_data



class CadastroForm(forms.ModelForm):

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
    tipo_sanguineo = forms.CharField(max_length=20)
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

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ['nome', 'data_realizacao', 'resultado']

class ReceituarioForm(forms.ModelForm):
    class Meta:
        model = Receituario
        fields = ['nome', 'data_emissao', 'conteudo']



