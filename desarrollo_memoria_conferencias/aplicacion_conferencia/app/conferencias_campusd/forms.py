from django import forms
from app.videos_de_conferencias.models import Video
from app.presentacion_de_conferencias.models import Diapositiva, slides_ppt
from app.conferencias_campusd.models import Conferencia


class DiapositivaForm(forms.ModelForm):

	class Meta:
		model = Diapositiva
		
		fields = [
				'diapo',
				'xml',
		]
		labels = {
				'diapo'  : 'Selecciona un archivo',
				'xml'	 :  'Seleccione un archivo'	
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


class ConferenciaForm(forms.ModelForm):
	
	class Meta:
		model = Conferencia

		fields = [
				'titulo',
				'autor',
				'descripcion',
				'categoria',
				'tags',
		]
		labels = {
				'titulo'	: 'Ingrese Titulo de Conferencia',
				'autor'		: 'Ingrese nombre de Autor',
				'descripcion'	: 'Agregue Descripcion',
				'categorias'	: 'Selecione Categoria',
				'tags'		: 'lecciones los Tags',
		}
		widget = {
				'titulo' : forms.CharField(max_length=100),
				'autor' : forms.CharField(max_length=100),
				'descripcion' : forms.Textarea,
		}


		
class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))		



