from django.contrib import admin

# Register your models here.
from .models import Restaurantes, RestauranteImg

class AdminRestaurante(admin.ModelAdmin):
	list_display = ('nombre', 'precio', 'descripcion', 'imagen', 'precio')
	search_fields = ('nombre','descripcion')

admin.site.register(Restaurantes, AdminRestaurante)
admin.site.register(RestauranteImg)