from django import forms
from .models import Usuario, Producto, Categoria, Objetivo


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
        fields = [
            'nombre'
        ]
        labels = {
            'name': 'Nombre del producto'
        }


class SearchCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = [
            'nombre'
        ]
        labels = {
            'name': 'Nombre del producto'
        }

DEMO_CHOICES =(
    ("1", "Bajar de peso"),
    ("2", "Subir de peso"),
    ("3", "Tonificar"),
    ("4", "Sentirme bien"),
)

class InputForm(forms.Form):
    cedula = forms.CharField(max_length=200)
    nombre = forms.CharField(max_length=200)
    edad = forms.IntegerField()
    estatura = forms.IntegerField()
    peso = forms.IntegerField()
    objetivos = forms.MultipleChoiceField(choices = DEMO_CHOICES)