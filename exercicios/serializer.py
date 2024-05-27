from rest_framework import serializers
from exercicios.models import Exercicio

class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ['uuid', 'nome', 'repeticoes', 'descricao']