from django.contrib import admin
from app.videos_de_conferencias.models import Video #, url_video

class VideoAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'url_video', 'titulo', 'autor' ,'duracion', 'imagen', 'activo')
	
admin.site.register(Video, VideoAdmin)

#admin.site.register(url_video)

# Register your models here.
