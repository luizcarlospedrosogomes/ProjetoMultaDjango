from django.db import models


# Create your models here.
class Usuario(models.Model):
	nome = models.CharField(max_length=200)
	cpf  = models.CharField(max_length=200)

	"""class Meta:
		ordering = ['nome']
		verbose_name = 'usuario'
		verbose_name_plural = 'usuarios'
	
	def __str__(self):
		return self.nome
		
"""