from cryptography.hazmat.primitives.kdf.kbkdf import Mode
from django.conf.locale import de
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora, Autor, Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"



class LivroListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
