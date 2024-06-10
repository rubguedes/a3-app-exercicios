from rest_framework import viewsets, generics
from usuario.models import Usuario, Historico
from usuario.serializer import UsuarioSerializer, HistoricoSerializer, HistoricoExercicioUsuarioSerializer, UsuarioSerializerv2

# Create your views here.
class UsuariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os usuarios"""
    queryset = Usuario.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UsuarioSerializerv2
        else:
            return UsuarioSerializer

class HistoricosViewSet(viewsets.ModelViewSet):
    """Exibindo o histórico"""
    queryset = Historico.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch']
    serializer_class = HistoricoSerializer

class HistoricoExerciciosUsuario(generics.ListAPIView):
    """Listando o histórico de exercícios de um usuário"""
    def get_queryset(self):
        queryset = Historico.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = HistoricoExercicioUsuarioSerializer
