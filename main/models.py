from django.db import models

# Create your models here.
class contacto(models.Model):
  nombre = models.CharField(max_length=15)
  email = models.CharField(max_length=15)
  mensaje = models.CharField(max_length=15)