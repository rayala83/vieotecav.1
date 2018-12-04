from django import forms
from app.videos_de_conferencias.models import Video
from app.presentacion_de_conferencias.models import Diapositiva, imagen_ppt
from app.conferencias_campusd.models import Conferencia


class DiapositivaForm(forms.ModelForm):

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
		model = Video
		
		fields = [
				'url_video',		
		]
		labels = {
				'url_video'  : 'URL_video',
		}
		widget = {
				'url_video'  : forms.TextInput(attrs={'class':'form-control'}), 
		}
		
class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))		



class ConferenciaForm(forms.Form):
	ppt = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))