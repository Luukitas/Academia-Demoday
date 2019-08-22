from django.shortcuts import render
from django.shortcuts import redirect
from demo.models import Pessoa
from demo.models import Empresa
from demo.models import Exp_pessoa
from .forms import *

#inicio dos imports e da views para a pagina de perguntas
from .forms import PerguntaForm
from .forms import AlternativaForm 
from .models import Alternativa

def visualizar_perguntas(request):
    perguntas = Pergunta.objects.all()
    return render(request, 'visualizar_perguntas.html', { 'perguntas' : perguntas})

def pergunta_inserir(request):
    form_pergunta = PerguntaForm(request.POST)
    form_alternativas = [AlternativaForm(request.POST, prefix = str(i))for i in range(1, 6)]

    if(form_pergunta.is_valid() and all(form_alternativa.is_valid() for form_alternativa in form_alternativas)):
        pergunta = form_pergunta.save()
        for form_alternativa in form_alternativas:
            alternativa = form_alternativa.save(commit=False)
            alternativa.pergunta = pergunta
            alternativa.save()
        redirect('visualizar_perguntas.html') ####Posteriorment colocar outro template
    return render(request, 'pergunta_form.html', { 'form_pergunta' : form_pergunta, 'form_alternativas': form_alternativas})

def pergunta_atualizar(request, id):
    pergunta = Pergunta.objects.get(pk = id)
    form_pergunta = PerguntaForm(request.POST or None, instance = pergunta)
    form_alternativas = [AlternativaForm(request.POST or None, instance = alternativa, prefix = str(alternativa.id)) for alternativa in pergunta.alternativa.all()]

    if(form_pergunta.is_valid() and all(form_alternativa.is_valid() for form_alternativa in form_alternativas)):
        form_pergunta.save()
        for form_alternativa in form_alternativas:
            form_alternativa.save()
        redirect('pergunta_form.html') ####Posteriorment colocar outro template
    return render(request, 'pergunta_form.html', { 'form_pergunta' : form_pergunta, 'form_alternativas': form_alternativas})
    
# fim da views para a pagina de perguntas.

def index(request):
    return render(request, 'index.html')

def cadastrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')   
    else:
        form = UsuarioForm()

    return render(request, 'cadastro.html', {'form': form})

def login(request):
    contexto = {}
    if request.method == 'POST':
        email_form = request.POST.get('email')
        senha_form = request.POST.get('senha')
        usuario = Pessoa.objects.filter(email=email_form).first()
        # exp = Exp_pessoa.objects.filter(experiencia=usuario.id)
        
    
        if usuario is None:
            print('deu ruim usuario')
            contexto = {'msg': 'Usuario ou senha incorretos. Por favor, insira um correto ou cadastre-se'}
            return render(request, 'login.html', contexto)
        elif usuario.senha is None:
            print('deu ruim senha')
            contexto = {'msg': 'Usuario ou senha incorretos. Por favor, insira um correto ou cadastre-se'}
            return render(request, 'login.html', contexto)
        elif senha_form != usuario.senha:
            print('deu errado')
            contexto = {'msg': 'Usuario ou senha incorretos. Por favor, insira um correto ou cadastre-se'}
            return render(request, 'login.html', contexto)
        else:
            contexto = {
                'pessoa': usuario,
                # 'exp': exp,
            }
            return render(request, 'usuario.html', contexto)

    return render(request, 'login.html', {})

def usuario(request, id):
    pessoa = Pessoa.objects.filter(id=id).first()
    contexto = {
        'pessoa': pessoa
    }
    return render(request, 'usuario.html', contexto)

def cadastra_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')   
    else:
        form = EmpresaForm()

    return render(request, 'cad-empresa.html', {'form': form})

def sobre_nos(request):
    return render(request, 'home.html', {})