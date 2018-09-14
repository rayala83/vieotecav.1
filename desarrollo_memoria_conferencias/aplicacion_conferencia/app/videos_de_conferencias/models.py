from django.db import models
from datetime import datetime


class Video(models.Model):
	fecha = models.DateTimeField(default=datetime.now())
	titulo = models.CharField(max_length=300)
	autor = models.CharField(max_length = 300)
	duracion = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='media')
	activo = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.titulo
		
	class Meta:
		ordering = ["fecha"]
		verbose_name_plural = "Videos"
	
class url_video(models.Model):
	url_video = models.URLField(max_length = 150,)
	
	def __unicode__(self):
		return self.url_video
	
	class Meta:
		verbose_name_plural = "Urls"