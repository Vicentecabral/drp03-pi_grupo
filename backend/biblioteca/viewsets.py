from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from biblioteca.models import biblioteca

from biblioteca.serializers import bibliotecaSerializer


class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = biblioteca.objects.all()
    serializer_class = bibliotecaSerializer
    permission_classes = [AllowAny]