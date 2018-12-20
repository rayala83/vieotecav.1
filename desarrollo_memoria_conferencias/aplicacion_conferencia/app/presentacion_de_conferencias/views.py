from django.shortcuts import render
from app.presentacion_de_conferencias.models import Diapositiva, slides_ppt

# Create your views here. a modo de prueba agregue modelo de videos debo arreglar


def sinc(request, num):
	ppt = Diapositiva.objects.get(id=num)
	conferencia = ppt.conferencia_set.all()
	if conferencia.exists():
		slide = slides_ppt.objects.filter(id_diapo=ppt)
		if slide.exists():
			return render(request, 'sincronizar.html', {'conf' :conferencia, 'slide': slide})
		return render(request, 'sincronizar.html', {'conf' :conferencia, 'slide': slide})
	return redirect('app.conferencias_campusd.views.index')	





def presentacion(request,num):
    app = Diapositiva.objects.filter(id_video=num)
    if app.exists():
    	slide = slides_ppt.objects.filter(id_diapo=app)
    	if slide.exists():
    		return render(request, 'mis_presentaciones.html', {'app' :app, 'slide': slide})
    	return render(request, 'mis_presentaciones.html', {'app' :app, 'slide': slide})
    return redirect('app.conferencias_campusd.views.index')	