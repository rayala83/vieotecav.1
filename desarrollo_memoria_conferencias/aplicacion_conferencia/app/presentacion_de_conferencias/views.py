from django.shortcuts import render
from app.presentacion_de_conferencias.models import Diapositiva, slides_ppt
from app.videos_de_conferencias.models import Video
import numpy


# Create your views here. a modo de prueba agregue modelo de videos debo arreglar


def sinc(request, num):
    video = Video.objects.filter(conferencia_id=num)
    ppt = Diapositiva.objects.filter(conferencia_id=num)
    if ppt.exists():
        slides = slides_ppt.objects.filter(id_diapo=ppt)
        if slides.exists():
            tiempos=numpy.zeros((len(slides),3), dtype=int)
            tiempos[0,0]=0
            tiempos[0,1]=round(float(slides[0].duracion),0)
            tiempos[0,2]=round(float(slides[0].duracion),0)
            items=[]
            items.append([slides[0].slide.url,tiempos[0]])
            for i in range(1,len(slides)):
                tiempos[i,0]=tiempos[i-1,1]
                tiempos[i,1]=tiempos[i,0]+round(float(slides[i].duracion),0)
                tiempos[i,2]=round(float(slides[i].duracion),0)
                items.append([slides[i].slide.url,tiempos[i]])
            return render(request, 'sincronizar.html', {'conf' :video, 'items': items})
        return render(request, 'sincronizar.html', {'conf' :video, 'slide': slides})
    return redirect('app.conferencias_campusd.views.index')	





def conferencias(request,num):
    video = Video.objects.filter(conferencia_id=num)
    ppt = Diapositiva.objects.filter(conferencia_id=num)
    if ppt.exists():
        slides = slides_ppt.objects.filter(id_diapo=ppt)
        if slides.exists():
            tiempos=numpy.zeros((len(slides),3), dtype=int)
            tiempos[0,0]=0
            tiempos[0,1]=round(float(slides[0].duracion),0)
            tiempos[0,2]=round(float(slides[0].duracion),0)
            items=[]
            items.append([slides[0].slide.url,tiempos[0]])
            for i in range(1,len(slides)):
                tiempos[i,0]=tiempos[i-1,1]
                tiempos[i,1]=tiempos[i,0]+round(float(slides[i].duracion),0)
                tiempos[i,2]=round(float(slides[i].duracion),0)
                items.append([slides[i].slide.url,tiempos[i]])
            return render(request, 'mis_conferencias.html', {'conf' :video, 'items': items, 'slide': slides})
        return render(request, 'mis_conferencias.html', {'conf' :video, 'slide': slides})
    return redirect('app.conferencias_campusd.views.index')	