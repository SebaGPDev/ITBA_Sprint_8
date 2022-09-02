from django.db import models
from cliente.models import Cliente
from tarjeta.choices import marca_tarjetas, tipo_tarjetas


# Create your models here.

class Tarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True)
    tarjeta_numero = models.CharField(max_length=200)
    tarjeta_cvv = models.IntegerField()
    tarjeta_emision = models.CharField(max_length=255)
    tarjeta_expiracion = models.CharField(max_length=255)
    tarjeta_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    tarjeta_marca = models.CharField(max_length=10, choices=marca_tarjetas)
    tarjeta_tipo = models.CharField(max_length=10, choices=tipo_tarjetas)
    class Meta:
        verbose_name = "Tarjeta"
        verbose_name_plural = "Tarjetas"
        db_table = 'tarjeta'
    def __str__(self): 
        return str(self.tarjeta_numero)