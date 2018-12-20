from django.db import models


class Diapositiva(models.Model):
	diapo = models.FileField(upload_to='ppt')
		
	class Meta:
		ordering = ["diapo"]
		verbose_name_plural = "Diapositivas"
		
class slides_ppt(models.Model):
	slide = models.ImageField(upload_to='slides')
	id_diapo = models.ForeignKey(Diapositiva, on_delete=models.CASCADE)
	duracion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.slide	

	class Meta:
		ordering = ["slide"]
		verbose_name_plural = "slides"