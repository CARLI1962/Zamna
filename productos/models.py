from django.db import models

# Create your models here.
from django.db import models


class Alimento(models.Model):
    nombre=models.CharField(max_length=50)
    alacena=models.ForeignKey('mercado.Alacena', on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=200)
    peso = models.IntegerField(default=0)


