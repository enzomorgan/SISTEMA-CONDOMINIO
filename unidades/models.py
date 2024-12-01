from django.db import models

# Create your models here.

class Unidade(models.Model):
    bloco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    status = models.CharField(max_length=50, choices=[('ocupado', 'Ocupado'), ('vazio', 'Vazio')])

    def __str__(self):
        return f"{self.bloco} - {self.numero}"