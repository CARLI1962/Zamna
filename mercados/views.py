from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render
from .logic.logic_productos import get_all_productos, get_products_by_name, get_product_id, get_all_components_product
from .logic.logic_categoria import get_all_categorias, get_categorias_by_name
from django.core import serializers
from Zamna.auth0backend import getLogins, get_correo
from django.contrib.auth.decorators import login_required
from .forms import FirstTimeUser, InputForm
from .logic.logic_usuario import create_usuario, get_usuario_correo
from django.urls import reverse
from .logic.logic_componentes import get_all_componentes


def index(request):
    return HttpResponse("Hello, world. You're at the mercados index.")


def get_all_products(request):
    productos = get_all_productos()
    productos_list = serializers.serialize('json', productos)
    return HttpResponse(productos_list, content_type='application/json')


def get_product_name(request, name):
    try:
        print(name)
        productos = get_products_by_name(name)

        productos_list = serializers.serialize('json', productos)
        return HttpResponse(productos_list, content_type='application/json')
    except:
        return HttpResponse('paila socito')


@login_required()
def profile(request):
    try:
        correo = get_correo(request)
        usuario = get_usuario_correo(correo)
        print(usuario)
        return render(request, 'user.html')
    except Exception as e:
        print(e)
        return usuario_create(request)



@login_required()
def usuario_create(request):
    if request.method == 'POST':
        print('hey')
        form = FirstTimeUser(request.POST)
        if form.is_valid():
            correo = get_correo(request)
            print(correo)
            create_usuario(form, correo)
            return profile(request)
        else:
            print(form.errors)
    else:
        form = FirstTimeUser()
        print(form.fields)

    context = {
        'form': form
    }
    return render(request, 'home1.html', context)


@login_required()
def product_searched(request):
    name = request.GET.get('searching')
    productos = get_products_by_name(name)
    context ={'productos' : productos}
    return render(request, 'user.html', context)


@login_required()
def basket(request):
    correo = get_correo(request)
    usuario = get_usuario_correo(correo)
    productos = usuario.comprados.all()
    print(len(productos))
    context = {'productos': productos}
    return render(request, 'basket.html', context)


@login_required()
def recom(request):
    correo = get_correo(request)
    usuario = get_usuario_correo(correo)
    recomendados = usuario.recomendados.all()
    context = {'productos': recomendados}
    return render(request, 'recom.html', context)

@login_required()
def product_components(request, id):
    componentes = get_all_components_product(id)
    print(componentes)
    producto = get_product_id(id)
    context = {'producto': producto, 'componentes': componentes}
    return render(request, 'components.html', context)

@login_required()
def add_product_basket(request):
    productID = request.GET.get('productId')
    print(productID)
    producto = get_product_id(productID)
    correo = get_correo(request)
    usuario = get_usuario_correo(correo)
    usuario.comprados.add(producto)
    return HttpResponseRedirect(reverse('basket'))


