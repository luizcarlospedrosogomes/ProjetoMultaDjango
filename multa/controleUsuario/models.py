from django.db import models


# Create your models here.
class Usuario(models.Model):
	nome = models.CharField(max_length=200)
	cpf  = models.IntegerField(max_length=15)

class Multa(models.Model):
	titulo 	   		  = models.CharField(max_length=200)
	gravidade 		  = models.IntegerField(max_length=10)
	local    		  = models.CharField(max_length=200)
	numeros_de_pontos = models.IntegerField(max_length=10)
	