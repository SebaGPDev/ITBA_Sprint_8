from django.db import models
from argparse import BooleanOptionalAction


class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    cliente_nombre = models.CharField(max_length=255,verbose_name='Nombre')
    cliente_apellido = models.CharField(max_length=255, verbose_name='Apellido')
    cliente_dni = models.IntegerField(verbose_name='DNI')
    cliente_dob = models.DateField(verbose_name='Fecha de nacimiento', blank=True, null=True)
    cliente_email = models.EmailField(verbose_name='Email', blank=True, null=True)
    cliente_telefono = models.IntegerField(verbose_name='Telefono', blank=True, null=True)
    cliente_direccion = models.ForeignKey('Direccion', verbose_name='Direccion', on_delete=models.CASCADE, blank=True, null=True)
    cliente_tipo = models.ForeignKey('TipoCliente', verbose_name='Tipo cliente', on_delete=models.CASCADE, blank=True, null=True)
    branch = models.ForeignKey('Sucursal', verbose_name='Sucursal', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-cliente_id"]
        db_table = 'Cliente'

    def __str__(self):
        return str(self.cliente.dni)


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
        ordering = ["-direccion_id"]
        db_table = 'direccion'


    def __str__(self):
        return self.direccion_id


class Empleado(models.Model):
    empleado_id = models.AutoField(primary_key=True)
    empleado_nombre = models.CharField(max_length=255, verbose_name='Nombre')
    empleado_apellido = models.CharField(max_length=255, verbose_name='Apellido')
    empleado_dni = models.IntegerField(db_column='empleado_dni', verbose_name='DNI')
    empleado_direccion = models.ForeignKey(Direccion, verbose_name='Direccion', on_delete=models.CASCADE, blank=True, null=True)
    branch = models.ForeignKey('Sucursal', verbose_name='Sucursal',  on_delete=models.CASCADE, blank=True, null=True)
    empleado_fecha_contratacion = models.CharField(max_length=255, verbose_name='Fecha de contratacion')

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["-empleado_id"]
        db_table = 'empleado'

    def __str__(self):
        return self.self.empleado_dni


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.CharField(max_length=255)
    # branch_address = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        ordering = ["-branch_id"]
        db_table = 'sucursal'


    def __str__(self):
        return self.branch_name


class TipoCliente(models.Model):
    tipo_cliente_id = models.AutoField(primary_key=True)
    tipo_nombre = models.CharField(max_length=255, unique=True)
    tipo_tarjeta_debito = models.CharField(max_length=255)
    tipo_tarjeta_cretido = models.CharField(max_length=255)
    tipo_cuenta_corriente = models.CharField(max_length=255)
    tipo_chequera = models.IntegerField()
    tipo_cuenta_dolar = models.CharField(max_length=255,blank=True, null=True)
    tipo_cuenta_peso = models.CharField(max_length=255,blank=True, null=True)
    retiro_diario = models.CharField(max_length=255, blank=True, null=True)
    comision_transferencia = models.CharField(max_length=255, blank=True, null=True)
    recepcion = models.CharField(max_length=255, blank=True, null=True)
    monto_pre_aprobado = models.IntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Tipo cliente"
        verbose_name_plural = "Tipo clientes"
        ordering = ["-tipo_cliente_id"]
        db_table = 'tipo_cliente'
        
    def __str__(self):
        return self.tipo_nombre