from django.db import models
from cliente.models import Cliente
from cuenta.choices import tipo_cuentas

# Create your models here.
class Cuenta(models.Model):
    cuenta_id = models.AutoField(primary_key=True)
    cuenta_balance = models.IntegerField()
    cuenta_iban = models.CharField(max_length=255)
    tipo_cuenta = models.CharField(choices=tipo_cuentas, max_length=30)
    cuenta_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    

    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"
        db_table = 'cuenta'


    def __str__(self): 
        return str(self.cuenta_cliente)