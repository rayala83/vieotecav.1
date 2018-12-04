from django.db import models

# Create your models here.

from datetime import datetime


class Conferencia(models.Model):	
	fecha = models.DateTimeField(default=datetime.now())	
	video = models.CharField(max_length=300)
	ppt = models.CharField(max_length=300)
	titulo = models.CharField(max_length=300)
	inicio = models.CharField(max_length=100)
	fin = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.titulo
		
	class Meta:
		ordering = ["fecha"]