from django.db import models

# Create your models here.

class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    direccion_calle = models.CharField(max_length=255, verbose_name='Calle')
    direccion_numero = models.IntegerField(verbose_name='Numero')
    direccion_ciudad = models.CharField(max_length=255, verbose_name='Ciudad')
    direccion_provincia = models.CharField(max_length=255, verbose_name='Provincia')
    direccion_pais = models.CharField(max_length=255, verbose_name='Pais')

    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
        db_table = 'direccion'


    def __str__(self):
        return self.direccion_calle