from rest_framework import routers
from .viewsets import NichoViewSet, LivroViewSet, Professor_FuncionarioViewSet, AlunoViewSet, StatusEmprestimoViewSet, EmprestimoViewSet, LivroEmprestimoViewSet

router = routers.SimpleRouter()

router.register(r'nicho', NichoViewSet)
router.register(r'livro', LivroViewSet)
router.register(r'professor_funcionario', Professor_FuncionarioViewSet)
router.register(r'aluno', AlunoViewSet)
router.register(r'status_emprestimo', StatusEmprestimoViewSet)
router.register(r'emprestimo', EmprestimoViewSet)
router.register(r'livro_emprestimo', LivroEmprestimoViewSet)

urlpatterns = router.urls
