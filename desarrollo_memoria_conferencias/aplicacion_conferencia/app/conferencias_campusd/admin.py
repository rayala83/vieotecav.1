from django.contrib import admin
from app.conferencias_campusd.models import Conferencia, Categoria, Tags, Sincronizacion, intervalo

# Register your models here.


class ConferenciaAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'titulo', 'autor', 'categoria')

admin.site.register(Conferencia,ConferenciaAdmin)

class categoriaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'jerarquia')

admin.site.register(Categoria, categoriaAdmin)

admin.site.register(Tags)

admin.site.register(Sincronizacion)

class intervaloAdmin(admin.ModelAdmin):
	list_display = ('id_sinc', 'inicio', 'fin')

admin.site.register(intervalo, intervaloAdmin)