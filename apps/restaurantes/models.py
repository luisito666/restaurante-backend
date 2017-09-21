import os

from rest import settings

from django.db import models


class Restaurantes(models.Model):
	nombre = models.CharField(max_length=150)
	direccion = models.CharField(max_length=150)
	descripcion = models.TextField()
	imagen = models.CharField(max_length=500)
	precio = models.CharField(max_length=150)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = 'Restaurante'
		verbose_name_plural = 'Restaurantes'

class RestauranteImg(models.Model):
	imagen = models.FileField('Subir Imagenes')