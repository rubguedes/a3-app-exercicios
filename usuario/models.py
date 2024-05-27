from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome_completo = models.CharField(max_length=40, null=False, blank=False, verbose_name="Nome")
    cpf = models.CharField(unique=True, max_length=11, null=False, blank=False, verbose_name="CPF")
    data_nascimento = models.DateField(blank=False, null=False, verbose_name="Data de Nascimento")
    telefone = models.CharField(max_length=11, null=False, blank=False, unique=True, verbose_name="Contato")
    email = models.EmailField(null=False, blank=False, unique=True, verbose_name="Email")
    senha = models.CharField(max_length=100, null=False, blank=False, verbose_name="Senha")
    historico = models.TextField(blank=True)

    def __str__(self):
        return self.nome_completo
    

class Historico(models.Model):
    usuario = Usuario()
    data = models.DateField(auto_now_add=True)
    exercicios = []