from rest_framework import serializers
from usuario.models import Usuario, Historico

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = []

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        exclude = []

class HistoricoExercicioUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        exclude = []

class UsuarioSerializerv2(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['senha']

