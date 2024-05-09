from django.db import models

# Create your models here.
class Reservas(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    cancha=models.CharField(max_length=50)
    fecha=models.DateField()
    hora=models.TimeField()
    duracion=models.IntegerField()
    cel=models.CharField(max_length=50)
    pago = models.BooleanField(default=False)
    

class Login(models.Model):
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)