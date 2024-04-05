from rest_framework import serializers
from .models import Nicho, Livro, Professor_Funcionario, Aluno, StatusEmprestimo, Emprestimo, LivroEmprestimo

class NichoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nicho
        fields = ['id_nicho', 'numero_nicho', 'local', 'observacao']
        read_only_fields = ['id_nicho']

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id_livro', 'nome_do_livro', 'autor', 'tipo', 'quantidade_exemplar', 'saldo_exemplar', 'id_nicho', 'observacao_livro']

class Professor_FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor_Funcionario
        fields = ['id_professor_funcionario', 'tipo_professor_funcionario', 'nome_do_professor_funcionario', 'cpf', 'telefone', 'email', 'data_registro', 'ativo']

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id_aluno', 'tipo_aluno', 'nome_do_aluno', 'ra', 'telefone', 'email', 'data_registro', 'ativo']

class StatusEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusEmprestimo
        fields = ['id_status', 'status']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['id_emprestimo', 'id_usuario_aluno', 'id_usuario_professor', 'data_emprestimo', 'data_devolucao']

class LivroEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivroEmprestimo
        fields = ['id_livro', 'id_emprestimo', 'quantidade', 'id_status']
