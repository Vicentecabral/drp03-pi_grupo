from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.core.exceptions import ValidationError
from validate_docbr import CPF  # Esta importação requer a instalação do pacote 'validate-docbr'



# Create your models here


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
        return f'{self.nome_do_livro} - Quantidade: {self.quantidade_exemplar}'

##########################################
class Professor_Funcionario(models.Model):
    TIPO_PROFESSOR_FUNCIONARIO_CHOICES = (
        ('Professor', 'Professor'),
        ('Funcionario', 'Funcionário'),
    )

    id_professor_funcionario = models.AutoField(primary_key=True)
    tipo_professor_funcionario = models.CharField(max_length=20, choices=TIPO_PROFESSOR_FUNCIONARIO_CHOICES, default='Professor')
    nome_do_professor_funcionario = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True, null=True)  # Mudança para 14 caracteres devido à formatação do CPF
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    data_registro = models.DateField(auto_now_add=True)  # Pega a data atual automaticamente
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'professor_funcionario'

    def __str__(self):
        return self.nome_do_professor_funcionario  # Definindo a representação como o nome do usuário

    def clean(self):
        # Validar o CPF utilizando a biblioteca validate-docbr
        cpf_validator = CPF()
        if self.cpf and not cpf_validator.validate(self.cpf):
            raise ValidationError('CPF inválido. Certifique-se de inserir um CPF válido.')

    def save(self, *args, **kwargs):
        self.clean()  # Chama o método clean para validar o CPF antes de salvar
        super().save(*args, **kwargs)  # Chama o método save padrão para salvar o objeto


##########################################
class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    tipo_aluno = models.CharField(max_length=20, default='Aluno')
    nome_do_aluno = models.CharField(max_length=150)
    ra = models.CharField(max_length=15, null=True)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    data_registro = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

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
from django.db import models
from .models import Aluno, Professor_Funcionario

class Emprestimo(models.Model):
    id_emprestimo = models.AutoField(primary_key=True)
    STATUS_CHOICES = (
        ('Aberto', 'Aberto'),
        ('Concluido', 'Concluido'),
    )
    id_usuario_aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='emprestimos_aluno',
        null=True,
        blank=True
    )
    id_usuario_professor = models.ForeignKey(
        Professor_Funcionario,
        on_delete=models.CASCADE,
        related_name='emprestimos_professor',
        null=True,
        blank=True
    )
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField()
    situacao_emprestimo = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aberto')

    class Meta:
        db_table = 'emprestimo'

    def __str__(self):
        if self.id_usuario_aluno:
            return f'Emprestimo {self.id_emprestimo} | Aluno {self.id_usuario_aluno.nome_do_aluno}'
        elif self.id_usuario_professor:
            return f'Emprestimo {self.id_emprestimo} | Professor/Funcionário {self.id_usuario_professor.nome_do_professor_funcionario}'
        return f'Emprestimo {self.id_emprestimo}'


##############################################
class LivroEmprestimo(models.Model):
    id_livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    id_emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    id_status = models.ForeignKey(StatusEmprestimo, on_delete=models.CASCADE, default=1)

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




##############################################
class LivroEmprestimoInline(admin.TabularInline):
    model = LivroEmprestimo
    extra = 1  # Define o número inicial de formulários vazios exibidos para adicionar livros

class EmprestimoAdmin(admin.ModelAdmin):
    inlines = [LivroEmprestimoInline]

#########################################







