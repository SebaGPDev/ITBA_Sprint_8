from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from cliente.models import Cliente
from api.serializers import ClienteSerializer

from direccion.models import Direccion
from api.serializers import DireccionSerializer

from TipoCliente.models import TipoCliente
from api.serializers import ClienteTipoSerializer

from sucursal.models import Sucursal
from api.serializers import SucursalSerializer

from cuenta.models import Cuenta
from api.serializers import CuentaSerializer

from prestamo.models import Prestamo
from api.serializers import PrestamoSerializer

from tarjeta.models import Tarjeta
from api.serializers import TarjetaSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'clientes': reverse('clientes-list', request=request, format=format),
        'direcciones': reverse('direcciones-list', request=request, format=format),
        'sucursales': reverse('sucursales-list', request=request, format=format),
        'cuentas': reverse('cuentas-list', request=request, format=format),
        'prestamos': reverse('prestamos-list', request=request, format=format),
        'tarjetas' : reverse('tarjetas-list', request=request, format=format),
    })


class ClienteDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        serializer = ClienteSerializer(cliente, context={'request': request})
        if cliente:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ClienteList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(
            clientes, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class DireccionDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, pk):
        direccion = Direccion.objects.filter(pk=pk).first()
        serializer = DireccionSerializer(
            direccion, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        direccion = Direccion.objects.filter(pk=pk)
        serializer = DireccionSerializer(
            direccion, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class DireccionList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        direcciones = Direccion.objects.all()
        serializer = DireccionSerializer(
            direcciones, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ClienteTipoDetail(APIView):
    def get(self, request, pk):
        tipocliente = TipoCliente.objects.filter(pk=pk) 
        serializer = ClienteTipoSerializer(tipocliente, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)

class SucursalList(APIView):
    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = SucursalSerializer(sucursales, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SucursalDetail(APIView):
    def get(self, request, pk):
        sucursal = Sucursal.objects.filter(pk=pk)
        serializer = SucursalSerializer(sucursal, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CuentaList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request): 
        cuentas = Cuenta.objects.all()
        serializer = CuentaSerializer(cuentas, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
class CuentaDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        cuenta = Cuenta.objects.filter(pk=pk).first()
        serializer = CuentaSerializer(cuenta, context={'request': request})
        if cuenta:
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
class TipoCuentaDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        cuenta_tipo = TipoCuenta.objects.filter(pk=pk).first()
        serializer = TipoCuentaSerializer(cuenta_tipo, context={'request': request})
        if cuenta_tipo:
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
class PrestamoList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request): 
        prestamos = Prestamo.objects.all().order_by('loan_id') 
        serializer = PrestamoSerializer(prestamos, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None): 
        serializer = PrestamoSerializer(data=request.data, context={'request': request}) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PrestamoDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        prestamo = Prestamo.objects.filter(pk=pk).first()
        serializer = PrestamoSerializer(prestamo, context={'request': request})
        if prestamo:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk): 
        prestamo = Prestamo.objects.filter(pk=pk).first() 
        if prestamo: 
            serializer = PrestamoSerializer(prestamo, context={'request': request}) 
            prestamo.delete() 
            return Response(serializer.data, status=status.HTTP_200_OK) 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class PrestamoSucursalList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk): 
        sucursal = Sucursal.objects.filter(pk=pk).first()
        asociados = Cliente.objects.filter(branch = sucursal)
        prestamos = []
        for cliente in asociados:
            prestamos += Prestamo.objects.filter(customer = cliente)
        serializer = PrestamoSerializer(prestamos, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)

class TipoPrestamoDetail(APIView):
    def get(self, request, pk):
        tipo_prestamo = TipoPrestamo.objects.filter(pk=pk)
        serializer = PrestamoTipoSerializer(tipo_prestamo, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TarjetasList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        tarjetas = Tarjeta.objects.all()
        serializer = TarjetaSerializer(tarjetas, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TarjetasDetail(APIView):
    def get(self, request, pk):
        tarjeta = Tarjeta.objects.filter(pk=pk)
        serializer = TarjetaSerializer(tarjeta, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # def get(self, request): 
    #     tarjetas = Tarjeta.objects.all()
    #     serializer = CuentaSerializer(cuentas, many=True, context={'request': request}) 
    #     return Response(serializer.data, status=status.HTTP_200_OK)    
# class TarjetasDetail(APIView):
#     def get(self, request, pk):
#         tarjeta = Tarjeta.objects.filter(pk=pk)
#         serializer = TarjetaSerializer(tarjeta, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class TarjetasMarcasDetail(APIView):
#     def get(self, request, pk):
#         marca = MarcaTarjeta.objects.filter(pk=pk)
#         serializer = MarcaTarjetaSerializer(marca, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)