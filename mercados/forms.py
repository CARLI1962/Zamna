from django import forms
from .models import Usuario, Producto, Categoria


class FirstTimeUser(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
            'id',
            'nombre',
            'edad',
            'altura',
            'peso',
            'objetivos'
        ]
        labels = {
            'id': 'Cedula',
            'nombre': 'Nombre',
            'edad': 'Edad',
            'altura': 'Altura en cm',
            'peso' : 'Peso en kg',
            'objetivos': 'Objetivos'
        }


class SearchProductByName(forms.ModelForm):

    class Meta:
        model = Producto
        field = [
            'nombre'
        ]
        labels = {
            'name': 'Nombre del producto'
        }


class SearchCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        field = [
            'nombre'
        ]
        labels = {
            'name': 'Nombre del producto'
        }
