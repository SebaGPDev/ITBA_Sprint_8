from django.db import models
from cuenta.models import Cuenta

# Create your models here.

class Movimiento(models.Model):
    movimiento_transaccion_id = models.AutoField(primary_key=True)
    movimiento_cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, blank=True, null=True)
    movimiento_tipo_operacion = models.CharField(max_length=255, null=True, blank=True)
    movimiento_monto = models.IntegerField()
    movimiento_cambiado = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"
        db_table = 'movimientos'

    def __str__(self): 
        return str(self.movimiento_transaccion_id)