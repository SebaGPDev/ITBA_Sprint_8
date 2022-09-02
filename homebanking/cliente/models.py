from django.db import models
from direccion.models import Direccion
from TipoCliente.models import TipoCliente
from sucursal.models import Sucursal


class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    cliente_nombre = models.CharField(max_length=255,verbose_name='Nombre')
    cliente_apellido = models.CharField(max_length=255, verbose_name='Apellido')
    cliente_dni = models.IntegerField(verbose_name='DNI')
    cliente_dob = models.DateField(verbose_name='Fecha nacimiento', blank=True, null=True)
    cliente_email = models.EmailField(verbose_name='Email', blank=True, null=True)
    cliente_telefono = models.IntegerField(verbose_name='Telefono', blank=True, null=True)
    cliente_direccion = models.ForeignKey(Direccion, verbose_name='Direccion', on_delete=models.CASCADE, blank=True, null=True)
    cliente_tipo = models.ForeignKey(TipoCliente, verbose_name='Tipo cliente', on_delete=models.CASCADE, blank=True, null=True)
    branch = models.ForeignKey(Sucursal, verbose_name='Sucursal', on_delete=models.CASCADE, blank=True, null=True)



    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = 'Cliente'

    def __str__(self):
        return str(self.cliente_dni)