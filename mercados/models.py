from django.db import models
from django.contrib.postgres.fields import ArrayField


class Usuario(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    edad = models.SmallIntegerField()
    altura = models.SmallIntegerField()
    peso = models.SmallIntegerField()
    objetivos = ArrayField(models.CharField(max_length=20, blank=True), default=list)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=240)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    #Relaciones
    sustitutos = models.ManyToManyField('self')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Producto_componente(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    cantidad = models.FloatField()
    #Relaciones
    componente = models.ForeignKey('Componente', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)

class Componente(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=240)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


