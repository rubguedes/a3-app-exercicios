from rest_framework import serializers
from usuario.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome_completo', 'cpf', 'data_nascimento', 'telefone', 'email', 'historico']