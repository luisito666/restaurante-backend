from django.shortcuts import render # Response
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
#importando cosas mias
from .models import Restaurantes, RestauranteImg
from .serializador import SerialHoteles, SerialRestaurantes, UploadSerializers
# Create your views here.
import time
from random import randint
from rest_framework.decorators import api_view


# Create your views here.
def inicio(request):
	context = {'algo':'algo'}
	return render(request, 'index.html', context)


class ImgUpload(viewsets.ModelViewSet):
	queryset = RestauranteImg.objects.all()
	serializer_class = UploadSerializers

class RestauranteLista(generics.ListCreateAPIView):
	queryset = Restaurantes.objects.all()
	serializer_class = SerialHoteles
	
	def get(self, request):
		#time.sleep(5)
		serializer = SerialRestaurantes(Restaurantes.objects.all(), many=True)		
		return Response({'status': 'success', 'data': serializer.data })
	
	def post(self, request, *args, **kwargs):		
		serializador = SerialRestaurantes(data = request.data)
		
		#serializador = SerialRestaurantes(data = request.data)
		if serializador.is_valid():
			serializador.save()
			return Response({'status':'success', 'message':'Restaurante creado correctamente'})
		return Response({'status':'error', 'message':'Restaurante no se ha creado'})
		"""a = Restaurantes()
		if request.method == 'POST':
			a.nombre = request.data['nombre']
			a.direccion = request.data['direccion']
			a.descripcion = request.data['descripcion']
			a.imagen = request.data['imagen']
			a.precio = request.data['precio']
			a.save()
			serializer = SerialRestaurantes(a)
			return Response({'status': 'success', 'message': serializer.data })
		else:
			return Response({'status': 'fail', 'message': 'nodata'})"""


class RestauranteDetalle(generics.RetrieveUpdateDestroyAPIView):
	queryset = Restaurantes.objects.all()
	serializer_class = SerialHoteles

	def get_object(self, **kwargs):
		try:
			return Restaurantes.objects.get(pk=self.kwargs['pk'])
		except:
			return False

	def get(self,request, *args, **kwargs):
		if self.get_object():
			self.object = self.get_object()
			serializer = SerialRestaurantes(self.object)
			return Response({'status': 'success', 'data': serializer.data })
		else:
			return Response({'status': 'false', 'data': 'nodata' })
	
	def post (self, request, *args, **kwargs):
		try:
			a = Restaurantes.objects.get(pk=self.kwargs['pk'])
		except Restaurantes.DoesNotExist:
			return Response({'status': 'false', 'data': 'nodata' })

		a.nombre = request.data['nombre']
		a.direccion = request.data['direccion']
		a.descripcion = request.data['descripcion']
		a.imagen = request.data['imagen']
		a.precio = request.data['precio']
		a.save()
		serializer = SerialRestaurantes(a)
		return Response({'status': 'success', 'message': serializer.data })


@api_view()
def ramdom_rest(request):
	contador = Restaurantes.objects.all().count()
	cantida = Restaurantes.objects.all()[:1].get()
	index_aleatorio = randint(cantida.pk, contador - 1)
	try:
		a = Restaurantes.objects.get(pk=index_aleatorio)
	except Restaurantes.DoesNotExist:
		return Response({'status':'fail','data': 'nodata' })
	serializer = SerialRestaurantes(a)
	return Response({'status':'success','data': serializer.data })

@api_view(['GET', 'POST'])
def delete_rest(request,pk):
	if request.method == "GET":
		try:
			a = Restaurantes.objects.get(pk=pk)
		except Restaurantes.DoesNotExist:
			return Response({'status':'fail','data': 'nodata' })

		a.delete()
		return Response({'status':'success', 'data': 'eliminado correctamente' })
	else:
		return Response({'status':'fail', 'data': 'nodata' })
	
	


"""def upload(request):
	if request.method == 'POST':"""
"""
class Upload(generics.RetrieveUpdateDestroyAPIView):
	queryset = Restaurantes.objects.all()
	serializer_class = SerialHoteles

	def post(self,request, *args, **kwargs)
		if request.method == 'POST':"""
