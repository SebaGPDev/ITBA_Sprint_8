from django.db import models
from .choices import tipo_clientes

class TipoCliente(models.Model):
    tipo_cliente_id = models.AutoField(primary_key=True)
    ipo_cliente = models.CharField(max_length=10, choices=tipo_clientes)
    tipo_tarjeta_debito = models.CharField(max_length=255)
    tipo_tarjeta_cretido = models.CharField(max_length=255)
    tipo_cuenta_corriente = models.CharField(max_length=255)
    tipo_chequera = models.IntegerField()
    tipo_cuenta_dolar = models.CharField(max_length=255,blank=True, null=True)
    tipo_cuenta_peso = models.CharField(max_length=255,blank=True, null=True)
    tipo_retiro_diario = models.CharField(max_length=255, blank=True, null=True)
    tipo_comision_transferencia = models.CharField(max_length=255, blank=True, null=True)
    tipo_recepcion = models.CharField(max_length=255, blank=True, null=True)
    tipo_monto_pre_aprobado = models.IntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Tipo cliente"
        verbose_name_plural = "Tipo clientes"
        db_table = 'tipo_cliente'
        
    def __str__(self):
        return str(self.tipo_cliente_id)