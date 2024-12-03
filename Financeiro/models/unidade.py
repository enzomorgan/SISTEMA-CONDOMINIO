from django.db import models

class Unidade(models.Model):
    numero = models.CharField(max_length=10)
    bloco = models.CharField(max_length=10)
    proprietario = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Unidade {self.numero} - Bloco {self.bloco}"
    
    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'