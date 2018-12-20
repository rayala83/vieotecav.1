from django.shortcuts import render
from app.conferencias_campusd.models import Conferencia

def video(request):	
	conferencias = Conferencia.objects.all()
	return render(request, 'detalle_video.html', {'conferencia' :conferencias})