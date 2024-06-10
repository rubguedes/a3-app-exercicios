from rest_framework import viewsets
from rest_framework import status
from exercicios.models import Exercicio
from exercicios.serializer import ExercicioSerializer
from rest_framework.response import Response

# Create your views here.
class ExerciciosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os exercicios"""
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response
