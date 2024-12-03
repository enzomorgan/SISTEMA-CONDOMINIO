from django.db import models
from django.contrib.auth.models import User

# Modelo para armazenar informações do perfil do morador
class PerfilMorador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relaciona o perfil ao usuário do Django
    telefone = models.CharField(max_length=15, blank=True, null=True)  # Telefone do morador
    endereco = models.CharField(max_length=255, blank=True, null=True)  # Endereço do morador
    data_nascimento = models.DateField(blank=True, null=True)  # Data de nascimento do morador
    unidade = models.CharField(max_length=10, unique=True)  # Unidade do morador (ex: A101)

    class Meta:
        verbose_name = "Perfil do Morador"
        verbose_name_plural = "Perfis dos Moradores"

    def __str__(self):
        return f"{self.user.username} - {self.unidade}"
    