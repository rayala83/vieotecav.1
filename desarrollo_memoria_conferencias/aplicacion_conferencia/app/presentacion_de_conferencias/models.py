from django.db import models
from datetime import datetime

class Diapositiva(models.Model):
	fecha = models.DateTimeField(default=datetime.now())
	titulo = models.CharField(max_length=30)
	diapo = models.FileField(upload_to='media')
	activo = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.titulo
		
	class Meta:
		ordering = ["fecha"]
		verbose_name_plural = "Diapositivas"