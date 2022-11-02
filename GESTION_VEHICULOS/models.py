from django.db import models

# Create your models here.

class vehiculo(models.Model):
    placa = models.CharField(max_length=20, null=True)
    modelo = models.CharField(max_length=20, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    kilometros = models.CharField(max_length=20, null=True, blank=True)