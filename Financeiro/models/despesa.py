from django.db import models

class Despesa(models.Model):
    CATEGORIAS = [
        ('MANUTENCAO', 'Manutenção'),
        ('UTILIDADE', 'Utilidade'),
        ('FUNCIONARIOS', 'Funcionários'),
        ('SEGURO', 'Seguro'),
        ('OUTROS', 'Outros')
    ]
    
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    pago = models.BooleanField(default=False)
    data_vencimento = models.DateField()
    
    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"
    
    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'