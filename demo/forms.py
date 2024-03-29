from django import forms
from proj import settings
from .models import *

#formulario do aplicativo de perguntas
from django.forms import ModelForm
from django.forms import Form
from django.forms import ModelChoiceField
from django.forms import Select
from django.forms import TextInput
from django.forms import Textarea
from demo.models import Pergunta
from demo.models import Disciplina
from demo.models import Nivel
#from demo.models import Ano
from demo.models import Area
from demo.models import Framework
from demo.models import Alternativa


class FiltroForm(Form):
    disciplina = ModelChoiceField(queryset = Disciplina.objects.all(), empty_label="Linguagem de programação?", required=False, widget=Select(attrs={'class': 'custom-select'}))#Isto define oque aparece quando a caixa de texto estiver vazia
    nivel = ModelChoiceField(queryset = Nivel.objects.all(), empty_label="Nivel?", required=False, widget=Select(attrs={'class': 'custom-select'}))
    #ano = ModelChoiceField(queryset = Ano.objects.all(), empty_label="Ano")
    area = ModelChoiceField(queryset = Area.objects.all(), empty_label="Area?", required=False, widget=Select(attrs={'class': 'custom-select'}))
    framework = ModelChoiceField(queryset = Framework.objects.all(), empty_label="Framework?", required=False, widget=Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = Pergunta
        fields = ['texto', 'disciplina', 'area', 'nivel', 'framework' ]
        widgets = {
            'texto' : Textarea(attrs={'class': 'form-question', 'placeholder': 'Escreva aqui a sua pergunta'}),
            }

#cria a form
class PerguntaForm(ModelForm):
    disciplina = ModelChoiceField(queryset = Disciplina.objects.all(), empty_label="Qual a linguagem de programação?", required=True, widget=Select(attrs={'class': 'custom-select'}))#Isto define oque aparece quando a caixa de texto estiver vazia
    nivel = ModelChoiceField(queryset = Nivel.objects.all(), empty_label="Qual o nivel de dificuldade da pergunta?", required=True, widget=Select(attrs={'class': 'custom-select'}))
    #ano = ModelChoiceField(queryset = Ano.objects.all(), empty_label="Ano da pergunta")
    area = ModelChoiceField(queryset = Area.objects.all(), empty_label="A pergunta é de qual area?", required=True, widget=Select(attrs={'class': 'custom-select'}))
    framework = ModelChoiceField(queryset = Framework.objects.all(), empty_label="Qual o Framework que a pergunta pertence?", required=True, widget=Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = Pergunta
        fields = ['texto', 'disciplina', 'area', 'nivel', 'framework' ]
        widgets = {
            'texto' : Textarea(attrs={'class': 'form-question', 'placeholder': 'Escreva aqui a sua pergunta'}),
            }


class AlternativaForm(ModelForm):
    class Meta:
        model = Alternativa
        fields = ['texto', 'correta'] #A pergunta não foi usada da models pois ela é realizada pelo usuário
        widgets = {'texto' : TextInput(attrs={'class': 'form-control', 'placeholder': 'insira o conteudo da alternativa'})}

#fim do app de perguntas

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'senha', 'profissao', 'img_perfil']

class EmpresaForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Empresa
        fields = ['nome', 'senha', 'cpf', 'estado', 'cidade', 'rua', 'numero', 'complemento', 'atuacao', 'img_perfil', 'descricao', 'linguagens']

class ExperienciaForm(forms.ModelForm):

    class Meta:
        model = Exp_pessoa
        fields = ['valores']

        