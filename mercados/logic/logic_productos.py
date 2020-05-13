from ..models import Producto


def get_all_productos():
    productos = Producto.objects.all()
    return productos


def get_products_by_name(name):
    productos = Producto.objects.all().filter(nombre__icontains=name)
    return productos
