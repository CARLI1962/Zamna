from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import  render
from .logic.logic_productos import get_all_productos, get_products_by_name
from .logic.logic_categoria import get_all_categorias, get_categorias_by_name
from django.core import serializers


def index(request):
    return HttpResponse("Hello, world. You're at the mercados index.")


def get_all_products(request):
    productos = get_all_productos()
    productos_list = serializers.serialize('json', productos)
    return HttpResponse(productos_list, content_type='application/json')


def get_product_name(request,name):
    try:
        print(name)
        productos = get_products_by_name(name)

        productos_list = serializers.serialize('json', productos)
        return HttpResponse(productos_list, content_type='application/json')
    except:
        return HttpResponse('paila socito')





