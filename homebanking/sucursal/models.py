from django.db import models
from direccion.models import Direccion

# Create your models here.
class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.CharField(max_length=255)
    branch_address = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        db_table = 'sucursal'


    def __str__(self): 
        return self.branch_name