from django.shortcuts import redirect, render
from alunos.models import Aluno
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import PessoaForm

# Create your views here.
def home(request):
    return render(request, 'index.html')


def cadastrar(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            return render(request, 'cadastrar.html')
        
        try:
            User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            return redirect('login')
        except:
            return render(request, 'index.html')


def logar(request):
    if request.user.is_authenticated:
        return render(request, 'area_usuario.html')

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome,
                            password=senha)
        if user:
            login(request, user)
            return render(request, 'area_usuario.html')
        else:
            return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('login')


def cadastroaluno(request):
    if request.method == "POST":
        foto = request.FILES.get("foto")
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        cpf = request.POST.get("cpf")
        rg = request.POST.get("rg")
        nascimento = request.POST.get("nascimento")
        ingresso = request.POST.get("ingresso")
        curso = request.POST.get("curso")

        aluno = Aluno(
            foto=foto,
            nome=nome,
            cpf=cpf,
            rg=rg,
            idade=int(idade),
            curso=curso,
            nascimento=nascimento,
            ingresso=ingresso,
        )
        aluno.save()

        return redirect('index')
    return render(request, 'cadastro_aluno.html')
    
    
def alunoscadastrados(request):
    if not request.user.is_authenticated:
        return redirect('login')
    alunos = Aluno.objects.all()
    keys = {
        'alunos': alunos,
    }
    return render(request, 'alunos_cadastrados.html', keys)