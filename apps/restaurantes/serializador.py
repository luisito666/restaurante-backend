import os
from rest import settings

from rest_framework import serializers as serializador
from .models import Restaurantes, RestauranteImg



class UploadSerializers(serializador.ModelSerializer):
	class Meta:
		model = RestauranteImg
		fields = ('pk', 'imagen')


class SerialHoteles(serializador.ModelSerializer):
	class Meta:
		model = Restaurantes
		fields = '__all__'


class SerialRestaurantes(serializador.Serializer):
	id = serializador.IntegerField(read_only=True)
	nombre = serializador.CharField(max_length=150)
	direccion = serializador.CharField(max_length=150)
	descripcion = serializador.CharField(max_length=150)
	imagen = serializador.CharField(max_length=500)
	precio = serializador.CharField(max_length=150)

	def create(self, validated_data):
		return Restaurantes.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.nombre = validated_data.get('nombre', instance.nombre)
		instance.direccion = validated_data.get('direccion', instance.direccion)
		instance.descripcion = validated_data.get('descripcion', instance.descripcion)
		instance.imagen = validated_data.get('imagen', instance.imagen)
		instance.precio = validated_data.get('precio', instance.precio)
		instance.save()
		return instance