from django.shortcuts import render
from app.videos_de_conferencias.models import Video

def video(request):	
	videos = Video.objects.all()
	return render(request, 'detalle_video.html', {'videos':	videos})