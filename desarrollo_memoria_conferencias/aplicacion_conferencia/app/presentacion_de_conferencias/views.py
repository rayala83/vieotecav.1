from django.shortcuts import render
from app.videos_de_conferencias.models import Video
from app.presentacion_de_conferencias.models import Diapositiva, imagen_ppt

# Create your views here. a modo de prueba agregue modelo de videos debo arreglar

def presentacion(request,num):
    app = Diapositiva.objects.filter(id_video=num)
    if app.exists():
    	slide = imagen_ppt.objects.filter(id_diapo=app)
    	if slide.exists():
    		return render(request, 'mis_presentaciones.html', {'app' :app, 'slide': slide})
    	return render(request, 'mis_presentaciones.html', {'app' :app, 'slide': slide})
    return redirect('app.conferencias_campusd.views.index')	