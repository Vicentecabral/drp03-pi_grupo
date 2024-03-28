from django.contrib import admin
from .models import Nicho, Livro, Aluno, StatusEmprestimo, Emprestimo, LivroEmprestimo, ConsultaLivroAdmin, EmprestimoAdmin



# Register your models here.

admin.site.register(Nicho)
admin.site.register(Livro, ConsultaLivroAdmin)
admin.site.register(Aluno)
admin.site.register(StatusEmprestimo)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(LivroEmprestimo)


