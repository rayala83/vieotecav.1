from django.db import models
from app.conferencias_campusd.models import Conferencia


class Video(models.Model):
	url_video = models.URLField(max_length=150)
	duracion = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='img_youtube')
	conferencia = models.OneToOneField('conferencias_campusd.Conferencia',on_delete=models.CASCADE)
	
	def __unicode__(self):
		return self.url_video
		
	class Meta:
		ordering = ["url_video"]
		verbose_name_plural = "Videos"