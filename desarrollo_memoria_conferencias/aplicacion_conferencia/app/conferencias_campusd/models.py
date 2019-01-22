from django.db import models

# Create your models here.

from datetime import datetime
from app.videos_de_conferencias.models import Video
from app.presentacion_de_conferencias.models import Diapositiva, slides_ppt


class Categoria(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=300)
	jerarquia = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.nombre
	
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Categorias"

		
class Tags(models.Model):
	nombre = models.CharField(max_length=10)
	
	def __unicode__(self):
		return self.nombre
		
	class Meta:
		verbose_name_plural = "Tags"


class Conferencia(models.Model):	
	fecha = models.DateTimeField(default=datetime.now())	
	video = models.ForeignKey('videos_de_conferencias.Video', on_delete=models.CASCADE)
	ppt = models.ForeignKey('presentacion_de_conferencias.Diapositiva', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=30)
	autor = models.CharField(max_length = 50)
	descripcion = models.CharField(max_length=500)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tags)
	activo = models.BooleanField(default=True)

	
	def __unicode__(self):
		return self.titulo
		
	class Meta:
		ordering = ["fecha"]
		verbose_name_plural = "Conferencias"



class Sincronizacion(models.Model):
	conferencia = models.ForeignKey(Conferencia, on_delete=models.CASCADE)

	def __unicode__(self):
		return self.conferencia

	class Meta:
		ordering = ["conferencia"]
		verbose_name_plural = "Sincronizaciones"


class intervalo(models.Model):
	id_sinc = models.ForeignKey(Sincronizacion, on_delete=models.CASCADE)
	id_slide_ppt = models.ForeignKey('presentacion_de_conferencias.slides_ppt', on_delete=models.CASCADE)
	acomulado = models.CharField(max_length=100)
	fin = models.CharField(max_length=100)

	def __unicode__(self):
		return self.id_sinc

	class Meta:
		ordering = ["id_slide_ppt"]
		verbose_name_plural = "Intervalos"