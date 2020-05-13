from ..models import Categoria


def get_all_categorias():
    categorias = Categoria.object.all()
    return categorias


def get_categorias_by_name(name):
    categorias = Categoria.objects.all().filter(nombre__icontains=name)
    return categorias

