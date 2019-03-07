from django.shortcuts import render
from app.presentacion_de_conferencias.models import Diapositiva, slides_ppt
from app.videos_de_conferencias.models import Video



# Create your views here. a modo de prueba agregue modelo de videos debo arreglar


def sinc(request, num):
	video = Video.objects.filter(conferencia_id=num)
	ppt = Diapositiva.objects.filter(conferencia_id=num)
	if ppt.exists():
		slide = slides_ppt.objects.filter(id_diapo=ppt)
		if slide.exists():
			return render(request, 'sincronizar.html', {'conf' :video, 'slide': slide})
		return render(request, 'sincronizar.html', {'conf' :video, 'slide': slide})
	return redirect('app.conferencias_campusd.views.index')	





def conferencias(request,num):
    video = Video.objects.filter(conferencia_id=num)
    ppt = Diapositiva.objects.filter(conferencia_id=num)
    if ppt.exists():
        slide = slides_ppt.objects.filter(id_diapo=ppt)
        if slide.exists():
    		return render(request, 'mis_conferencias.html', {'conf' :video, 'slide': slide})
    	return render(request, 'mis_conferencias.html', {'conf' :video, 'slide': slide})
    return redirect('app.conferencias_campusd.views.index')	