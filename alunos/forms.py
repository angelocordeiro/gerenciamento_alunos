from django import forms
from .models import Aluno


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('nome', 'idade', 'curso',
                  'cpf', 'rg', 'nascimento', 'ingresso', 'foto')