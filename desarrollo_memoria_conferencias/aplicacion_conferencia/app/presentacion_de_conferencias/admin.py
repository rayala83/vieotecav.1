from django.contrib import admin
from app.presentacion_de_conferencias.models import Diapositiva

class PPTAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'titulo', 'diapo', 'activo')
	
admin.site.register(Diapositiva, PPTAdmin)

# Register your models here.
