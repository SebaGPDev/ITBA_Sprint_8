from rest_framework import serializers
from cliente.models import Cliente
from direccion.models import Direccion
from TipoCliente.models import TipoCliente
from sucursal.models import Sucursal
from cuenta.models import Cuenta
from movimiento.models import Movimiento
from prestamo.models import Prestamo
from tarjeta.models import Tarjeta
# , TarjetaMarca

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        read_only_fields = ("cliente_id",)

class DireccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'
        read_only_fields = ("direccion_id",)
        
class ClienteTipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoCliente
        fields = '__all__'
        
class SucursalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'
        
class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'

class PrestamoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'
        
# class PrestamoTipoSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = TipoPrestamo
#         fields = '__all__'
        
class TarjetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarjeta
        fields = '__all__'