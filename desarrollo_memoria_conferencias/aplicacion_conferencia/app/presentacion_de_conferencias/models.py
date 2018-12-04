from django.db import models
from datetime import datetime
from app.videos_de_conferencias.models import Video

class Diapositiva(models.Model):
	fecha = models.DateTimeField(default=datetime.now())
	titulo = models.CharField(max_length=30)
	id_video = models.ForeignKey('videos_de_conferencias.Video', on_delete=models.CASCADE,)
	diapo = models.FileField(upload_to='media/ppt')
	activo = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.titulo
		
	class Meta:
		ordering = ["fecha"]
		verbose_name_plural = "Diapositivas"
		
class imagen_ppt(models.Model):
	imagen = models.ImageField(upload_to='media/fotos')
	id_diapo = models.ForeignKey(Diapositiva, on_delete=models.CASCADE)
	duracion = models.CharField(max_length=100)
	
	def __unicode__(self):
		return unicode(self.imagen)