from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
#from .models import Nicho  # Importando o modelo Nicho para a chave estrangeira
# Create your models here.

#TABELAS
##############################################
class Nicho(models.Model):
    id_nicho = models.BigAutoField(primary_key=True)
    numero_nicho = models.PositiveIntegerField()
    local = models.CharField(max_length=100, null=True)
    observacao = models.TextField(null=True)

    class Meta:
        db_table = 'nicho'

    def __str__(self):
        return f'Nicho {self.numero_nicho}'  # Personalizando a representação do objeto

##############################################
class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    nome_do_livro = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100, null=True)  # Permitindo valores nulos
    quantidade_exemplar = models.IntegerField()
    saldo_exemplar = models.IntegerField()
    id_nicho = models.ForeignKey(Nicho, on_delete=models.CASCADE)
    observacao_livro = models.TextField(null=True)  # Permitindo valores nulos

    class Meta:
        db_table = 'livro'

    def __str__(self):
        return self.nome_do_livro  # Definindo a representação como o nome do livro

##############################################
class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome_do_aluno = models.CharField(max_length=150)
    ra = models.CharField(max_length=15, null=True)
    serie = models.CharField(max_length=10, null=True)  # Permitindo valores nulos
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        db_table = 'aluno'

    def __str__(self):
        return self.nome_do_aluno  # Definindo a representação como o nome do aluno


##############################################
class StatusEmprestimo(models.Model):
    id_status = models.AutoField(primary_key=True)
    STATUS_CHOICES = (
        ('Emprestado', 'Emprestado'),
        ('Devolvido', 'Devolvido'),
        ('Extraviado', 'Extraviado'),
        ('Reservado', 'Reservado'),
        ('Aguardando_retirada', 'Aguardando Retirada'),
        ('Em_processamento', 'Em Processamento'),
        ('Vencido', 'Vencido'),
        ('Renovado', 'Renovado'),
        ('Danificado', 'Danificado'),
        ('Em_analise', 'Em Análise'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    class Meta:
        db_table = 'statusemprestimo'

    def __str__(self):
        return self.status

##############################################
class Emprestimo(models.Model):
    id_emprestimo = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()

    class Meta:
        db_table = 'emprestimo'

    def __str__(self):
        return f'Emprestimo {self.id_emprestimo} | Aluno {self.id_aluno.nome_do_aluno}'


##############################################
class LivroEmprestimo(models.Model):
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    id_emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    id_status = models.ForeignKey(StatusEmprestimo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'livro_emprestimo'
        unique_together = ('id_livro', 'id_emprestimo')

    def __str__(self):
        return f'Livro {self.id_livro} | Empréstimo {self.id_emprestimo} | Quantidade {self.quantidade}'

##############################################
#CONSULTAS
##############################################

class ConsultaLivroAdmin(admin.ModelAdmin):
    search_fields = ['nome_do_livro', 'autor', 'tipo']

    def get_changelist_instance(self, request):
        changelist_instance = super().get_changelist_instance(request)
        changelist_instance.title = _('Consultar livro por Nome, Autor ou Tipo')
        return changelist_instance

from django.contrib import admin
from .models import Emprestimo, LivroEmprestimo


##############################################
class LivroEmprestimoInline(admin.TabularInline):
    model = LivroEmprestimo
    extra = 1  # Define o número inicial de formulários vazios exibidos para adicionar livros

class EmprestimoAdmin(admin.ModelAdmin):
    inlines = [LivroEmprestimoInline]

