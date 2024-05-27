from rest_framework import viewsets
from usuario.models import Usuario
from usuario.serializer import UsuarioSerializer

# Create your views here.
class UsuariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os exercicios"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer