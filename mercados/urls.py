from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.get_all_products, name='listaProductos'),
    path('profile/', views.profile, name='profile'),
    path('profile/q', views.product_searched, name='productosLista'),
    path('profile/basket/', views.basket, name='basket'),
    path('profile/p', views.add_product_basket, name='agregarProducto')
]