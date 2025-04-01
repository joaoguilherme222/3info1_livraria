from rest_framework import serializers

from core.models import Categoria, Editora, Autor, Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"