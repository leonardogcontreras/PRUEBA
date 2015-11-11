from django.db import models
from django.contrib.auth.models import User

class Perfil_Mascota(models.Model):
#    foto = models.ImageField()
    nombre = models.CharField(max_length=25, blank=False)
    raza = models.CharField(max_length=25, blank=False)
    color = models.CharField(max_length=25, blank=False)
    sexo = models.CharField(max_length=25, blank=False)
    descripcion = models.TextField(max_length=255, blank=False)
 
    def __str__(self):
       return self.nombre