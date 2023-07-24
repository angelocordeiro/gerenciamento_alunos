from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    
    path('login/', view=views.logar, name='login'),
    path('logout/', view=views.sair, name='logout'),
    path("alunoscadastrados/", view=views.alunoscadastrados, name='alunos_cadastrados'),
    path("cadastroaluno/", view=views.cadastroaluno, name='cadastro_aluno'),
    path("cadastrar/", view=views.cadastrar, name='cadastrar'),
]