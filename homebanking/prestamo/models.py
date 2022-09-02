from django.db import models
from cliente.models import Cliente
from .choices import tipo_prestamos

# Create your models here.

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(choices=tipo_prestamos, max_length=15)
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    loan_preapproval = models.IntegerField(null=True,blank=True)
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE,  blank=True, null=True)

    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos" 
        db_table = 'prestamo'


    def __str__(self): 
        return str(self.loan_id)