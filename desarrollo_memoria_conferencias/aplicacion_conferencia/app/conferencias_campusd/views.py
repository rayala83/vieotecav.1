from django.shortcuts import render, redirect

from app.conferencias_campusd.forms import  UploadForm, formVideo
from app.presentacion_de_conferencias.models import Diapositiva
from app.videos_de_conferencias.models import Video, url_video

import pafy



def index(request):
    return render(request, 'index.html')
	

	
def sinc(request):
    return render(request, 'sincronizar.html')
	
def guarda_url(request):
	if request.method == 'POST':
		form_url = formVideo(request.POST)
		formsub = UploadForm(request.POST, request.FILES)
		if form_url.is_valid() and formsub.is_valid():
			newVideo = url_video(url_video = request.POST['url_video'])
			newdoc = Diapositiva(titulo = request.POST['titulo'],diapo = request.FILES['diapo'])
			
			video = pafy.new(newVideo)
			prueba = Video(titulo = video.title, autor = video.author, duracion = video.duration, imagen = video.thumb)
			prueba.save()
			
			newVideo.save()
			newdoc.save()
			
			
		return redirect('/')
	else:
		form_url = formVideo()
		formsub = UploadForm()
	return render(request, 'subir_url_video.html', {'form_url':form_url, 'formsub': formsub})	
	
def subir_archivo(request):
	if request.method == 'POST':
		formsub = UploadForm(request.POST, request.FILES)
		if formsub.is_valid():
			newdoc = Diapositiva(titulo = request.POST['titulo'],diapo = request.FILES['diapo'])
			newdoc.save()
		return redirect('/')
	else:
		formsub = UploadForm()
	return render(request, 'cargar_ppt.html', {'formsub': formsub})