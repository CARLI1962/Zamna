from ..models import Producto, Producto_componente
from .logic_componentes import get_component

def get_all_productos():
    productos = Producto.objects.all()
    return productos


def get_products_by_name(name):
    productos = Producto.objects.all().filter(nombre__istartswith=name)
    return productos


def get_productos_sustitutos_producto(i):
    producto = Producto.objects.all().get(id=i)
    productos_sustitutos = producto.sustitutos.all()
    return productos_sustitutos


def get_product_id(i):
    producto = Producto.objects.all().get(id=i)
    return producto

def get_all_components_product(i):
    componentes = Producto_componente.objects.all().filter(producto=i)
    return componentes
