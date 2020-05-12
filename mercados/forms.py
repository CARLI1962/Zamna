from django import forms
from .models import Usuario


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
