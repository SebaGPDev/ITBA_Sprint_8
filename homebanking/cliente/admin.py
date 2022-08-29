from django.contrib import admin
from .models import Cliente, Direccion, Sucursal, Empleado, TipoCliente
    
admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Sucursal)
admin.site.register(Empleado)
admin.site.register(TipoCliente)