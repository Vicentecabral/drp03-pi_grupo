from django.contrib import admin
#from django.db.utils import DatabaseError
#from django.contrib import messages
from .models import Nicho, Livro, Aluno, Professor_Funcionario, StatusEmprestimo, Emprestimo, LivroEmprestimo, ConsultaLivroAdmin, EmprestimoAdmin

admin.site.register(Nicho)
admin.site.register(Livro, ConsultaLivroAdmin)
admin.site.register(StatusEmprestimo)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(Aluno)
admin.site.register(Professor_Funcionario)
"""
class LivroEmprestimoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except DatabaseError as e:
            messages.error(request, "Erro ao salvar empréstimo: Saldo de exemplares insuficiente.")
"""
admin.site.register(LivroEmprestimo)
