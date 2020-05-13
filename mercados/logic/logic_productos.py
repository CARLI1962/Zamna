from ..models import Producto


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
