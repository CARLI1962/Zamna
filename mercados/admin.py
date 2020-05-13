from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Producto_componente)
admin.site.register(Componente)
admin.site.register(Categoria)
admin.site.register(Objetivo)