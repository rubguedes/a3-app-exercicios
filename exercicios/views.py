from rest_framework import viewsets
from exercicios.models import Exercicio
from exercicios.serializer import ExercicioSerializer

# Create your views here.
class ExerciciosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os exercicios"""
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer