from rest_framework import serializers

from biblioteca.models import Biblioteca


class BibliotecaSerializer(serializers.ModelSerializer):

    class Nicho:
        model = Biblioteca
        fields = ['id_nicho', 'numero_nicho', 'local', 'observacao']
        read_only_fields = ['id_nicho']