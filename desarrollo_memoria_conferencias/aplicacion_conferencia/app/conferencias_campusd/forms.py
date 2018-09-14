from django import forms
from app.videos_de_conferencias.models import Video, url_video
from app.presentacion_de_conferencias.models import Diapositiva


class UploadForm(forms.ModelForm):

	class Meta:
		model = Diapositiva
		
		fields = [
		'fecha', 
		'titulo',
		'diapo',
		'activo',		
		]
		labels = {
				'fecha'  : 'Fecha Creacion', 
				'titulo' : 'Titulo PPT',
				'diapo'  : 'Selecciona un archivo',
				'activo' : 'Estado',
		}
		widget = {
				'fecha'  : forms.TextInput(attrs={'class':'form-control'}), 
				'titulo'  : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ej: Escriba un Titulo'}),
				'activo'  : forms.Select(attrs={'class':'form-control'}), 
		}
		
class formVideo(forms.ModelForm):
	class Meta:
		model = url_video
		
		fields = [
				'url_video',		
		]
		labels = {
				'url_video'  : 'URL_video',
		}
		widget = {
				'url_video'  : forms.TextInput(attrs={'class':'form-control'}), 
		}