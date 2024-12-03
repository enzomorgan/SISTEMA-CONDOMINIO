from financeiro import models
from usuarios.models import PerfilMorador


class Casa(models.Model):
    numero_casa = models.CharField(max_length=10, unique=True)  # Número da unidade (ex: A101)
    morador = models.OneToOneField(PerfilMorador, on_delete=models.CASCADE, null=True, blank=True)  # Relacionamento com o perfil do morador
    ocupada = models.BooleanField(default=False)  # Indica se a unidade está ocupada
    
    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"