# coding=utf-8

from django.shortcuts import render, redirect

from django.views.generic.edit import FormView

from app.conferencias_campusd.forms import  DiapositivaForm, formVideo, FileFieldForm, ConferenciaForm

from app.presentacion_de_conferencias.models import Diapositiva, slides_ppt
from app.videos_de_conferencias.models import Video
from app.conferencias_campusd.models import Conferencia

import pafy

import convertapi
import tempfile

from django.core.files.images import ImageFile

convertapi.api_secret = 'lSaNbAz2Jv9Suib1'



def index(request):
    return render(request, 'index.html')

def intervalos(request):
    return render(request, 'prueba_resta.html')
	
	
	
def guarda_url(request):
	if request.method == 'POST':
		form_conf = ConferenciaForm(request.POST)
		form_video = formVideo(request.POST)
		form_ppt = DiapositivaForm(request.POST,request.FILES)

		print form_conf.is_valid()
		print form_video.is_valid()
		print form_ppt.is_valid()

		if form_conf.is_valid() and form_video.is_valid() and form_ppt.is_valid():
			
			

			newVideo = request.POST['url_video']
			video = pafy.new(newVideo)
			info_video = Video(url_video = video.videoid, duracion = video.duration, imagen = video.thumb)
			info_video.save()


			presentacion = Diapositiva(diapo =request.FILES['diapo'])
			presentacion.save()

			conferencia_nueva = form_conf.save(commit=False)
			conferencia_nueva.video = info_video
			conferencia_nueva = form_conf.save(commit=False)
			conferencia_nueva.ppt = presentacion
			conferencia_nueva.save()

			nombre = (conferencia_nueva.ppt.diapo).name
			print nombre

			duracion = conferencia_nueva.video.duracion
			print duracion
			
			result = convertapi.convert('jpg', {'File': '/vagrant/aplicacion_conferencia/media/' + nombre}, from_format = 'pptx').save_files(tempfile.gettempdir())
			print("The JPG saved to %s" % result)


			for f in result:
				foto = ImageFile(open(f))
				galeria = slides_ppt(slide = foto, id_diapo = conferencia_nueva.ppt, duracion = duracion)
				galeria.save()	
				print foto
		

			
		return redirect('/video')
	else:
		form_conf = ConferenciaForm()
		form_video = formVideo()
		form_ppt = DiapositivaForm()
	return render(request, 'subir_url_video.html', {'form_conf': form_conf,'form_video':form_video, 'form_ppt': form_ppt})	
	

	
class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'archivos_multiples.html' 
    success_url = '/' 

    def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		files = request.FILES.getlist('file_field')
		ppt_nueva = Diapositiva.objects.get(pk=61)
		print("The JPG saved to %s" % files)
		if form.is_valid():
		    for f in files:
		    	galeria = slides_ppt(imagen = f, id_diapo = ppt_nueva, inicio = ppt_nueva.url.duracion, fin = ppt_nueva.url.duracion)
		    	galeria.save()	
		    return self.form_valid(form)
		else:
		    return self.form_invalid(form)	
	
	
	
	
class subir_archivo(FormView):
	form_conferencia = ConferenciaForm
	template_name = 'cargar_ppt.html'
	success_url = '/' 

	def post(self, request, *args, **kwargs):
		form_conferencia = self.get_form_class()
		form = self.get_form(form_conferencia)
		files = request.FILES.getlist('ppt')
		if form.is_valid():

			
		# convertapi.convert('jpg', {'File': '/vagrant/aplicacion_conferencia/media/media/erroresen el desarrollo de softwares.pptx'}, 
		#	from_format = 'pptx').save_files('/vagrant/aplicacion_conferencia/media/prueba')

			return self.form_valid(form)
		else:
		    return self.form_invalid(form)