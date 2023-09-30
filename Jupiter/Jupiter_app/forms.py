from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'sobrenome', 'data_nascimento', 'endereco', 'complemento', 'email', 'telefone']
