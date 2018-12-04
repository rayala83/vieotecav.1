from django.contrib import admin
from app.conferencias_campusd.models import Conferencia

# Register your models here.


class ConferenciaAdmin(admin.ModelAdmin):
	list_display = ('fecha','video', 'ppt', 'titulo', 'inicio', 'fin' )

admin.site.register(Conferencia,ConferenciaAdmin)