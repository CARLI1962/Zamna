from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.get_all_products, name='listaProductos'),
    path('list/<str:name>', views.get_product_name, name='productosLista')
]