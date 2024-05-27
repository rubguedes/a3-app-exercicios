from django.db import models

# Create your models here.
class Exercicio(models.Model):
    uuid = models.CharField(max_length=36, blank=False, null=False, primary_key=True)
    nome = models.CharField(max_length=30, blank=False, null=False)
    repeticoes = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=300, blank=False, null=False)


    def __str__(self):
        return self.nome
    