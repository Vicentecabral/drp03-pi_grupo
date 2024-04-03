from rest_framework import routers

from biblioteca.viewsets import BibliotecaViewSet

router = routers.SimpleRouter()

router.register(r'biblioteca', BibliotecaViewSet, basename="biblioteca")

urlpatterns = router.urls