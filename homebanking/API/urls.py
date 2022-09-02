from django.contrib import admin
from django.urls import path

from .views import ClienteList, ClienteDetail, api_root, DireccionList, DireccionDetail, ClienteTipoDetail, SucursalList, SucursalDetail, CuentaList, CuentaDetail, TipoCuentaDetail, PrestamoList, PrestamoDetail, PrestamoSucursalList
from .views import TarjetasList, TarjetasDetail
# TarjetasDetail
# , TarjetasMarcasDetail
urlpatterns = [
        path('', api_root),
        path('clientes/', ClienteList.as_view(), name='clientes-list'),
        path('clientes/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),        
        path('direcciones/', DireccionList.as_view(), name='direcciones-list'),
        path('direcciones/<int:pk>/', DireccionDetail.as_view(), name='direccion-detail'),
        path('clientestipo/<int:pk>/', ClienteTipoDetail.as_view(), name='tipocliente-detail'),
        path('sucursales/', SucursalList.as_view(), name='sucursales-list'),
        path('sucursales/<int:pk>/', SucursalDetail.as_view(), name='sucursal-detail'),
        path('cuentas/', CuentaList.as_view(), name='cuentas-list'),
        path('cuenta/<int:pk>/', CuentaDetail.as_view(), name='cuenta-detail'),
        path('cuentatipo/<int:pk>/', TipoCuentaDetail.as_view(), name='tipocuenta-detail'),
        path('prestamos/', PrestamoList.as_view(), name='prestamos-list'),
        path('prestamo/<int:pk>/', PrestamoDetail.as_view(), name='prestamo-detail'),
        path('prestamossucursal/<int:pk>/', PrestamoSucursalList.as_view()),
        path('tarjetas/',TarjetasList.as_view(), name = 'tarjetas-list'),
        path('tarjetas/<int:pk>/',TarjetasList.as_view(), name = 'tarjeta-detail'),

        # path('tarjeta/<int:pk>/', TarjetasDetail.as_view(), name='tarjeta-detail'),
        # path('tarjetamarca/<int:pk>/', TarjetasMarcasDetail.as_view(), name='tarjetamarca-detail'),
]
