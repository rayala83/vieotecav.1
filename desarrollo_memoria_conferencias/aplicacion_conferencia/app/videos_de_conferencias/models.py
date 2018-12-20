from django.db import models


class Video(models.Model):
	url_video = models.URLField(max_length=150)
	duracion = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='img_youtube')
	
	def __unicode__(self):
		return self.url_video
		
	class Meta:
		ordering = ["url_video"]
		verbose_name_plural = "Videos"