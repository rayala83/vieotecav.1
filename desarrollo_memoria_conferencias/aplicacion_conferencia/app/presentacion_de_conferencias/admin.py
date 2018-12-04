from django.contrib import admin
from app.presentacion_de_conferencias.models import Diapositiva, imagen_ppt

class PPTAdmin(admin.ModelAdmin):
	list_display = ('id','fecha', 'titulo','id_video', 'diapo', 'activo')
	
admin.site.register(Diapositiva, PPTAdmin)

class imagenAdmin(admin.ModelAdmin):
	list_display = ('imagen','id_diapo', 'duracion')
admin.site.register(imagen_ppt, imagenAdmin)

# Register your models here.
