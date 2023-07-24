from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now_add=True)
    ativo = models.BooleanField('Está Ativo?', default=True)


    class Meta:
        abstract = True

class Aluno(Base):
    __table__ = 'aluno'
    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    curso = models.CharField('Curso', max_length=100)
    nascimento = models.DateField('Data de Nascimento')
    cpf = models.CharField('CPF', unique=True, max_length=11)
    rg = models.CharField('RG', unique=True, max_length=11)
    ingresso = models.DateField('Data de ingresso')
    foto = StdImageField('Imagem', upload_to='alunos', variations={'thumb': (124,124)})
    
    def __str__(self) -> str:
        return self.nome