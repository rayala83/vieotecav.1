from django.contrib import admin
from app.presentacion_de_conferencias.models import Diapositiva, slides_ppt

class PPTAdmin(admin.ModelAdmin):
	list_display = ('id','diapo', 'xml','conferencia')
	
admin.site.register(Diapositiva, PPTAdmin)

class slideAdmin(admin.ModelAdmin):
	list_display = ('slide','id_diapo', 'duracion')
admin.site.register(slides_ppt, slideAdmin)

# Register your models here.
