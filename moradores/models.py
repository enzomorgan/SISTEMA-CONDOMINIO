from django.db import models

# Create your models here.

class Morador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    unidade = models.ForeignKey('unidades.Unidade', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome