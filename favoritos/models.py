from django.db import models

# Create your models here.

class Favoritos(models.Model):
    nombre = models.CharField(max_length=50, blank=True)
    apellido = models.CharField(max_length=50, blank=True)
    url = models.URLField(max_length=200)
    
