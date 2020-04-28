from django.db import models


# Create your models here.
class Alacena(models.Model):
    numeroRegistro = models.AutoField(primary_key=True)

    def __str__(self):
        return self.numeroRegistro
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_Registro = models.DateTimeField('date published')
    correo = models.CharField(max_length=50)
    contraseña= models.CharField(max_length=50)
    #Relaciones
    alacena = models.OneToOneField(Alacena, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre



class Alimento(models.Model):
    numeroRegistro_alacena = models.OneToOneField(Alacena, on_delete=models.CASCADE, null=True, blank=True)
    nombre=models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    peso = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

