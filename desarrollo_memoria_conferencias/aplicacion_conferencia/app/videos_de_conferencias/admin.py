from django.contrib import admin
from app.videos_de_conferencias.models import Video 

class VideoAdmin(admin.ModelAdmin):
	list_display = ('url_video','duracion', 'imagen', 'conferencia')
	
admin.site.register(Video, VideoAdmin)

