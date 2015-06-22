from django.test import TestCase
from django.contrib.auth.models import User

from multa.controleUsuario.models import Multa, Usuario


#testa criacao de usuario na base de dados
class TesteMulta(TestCase):
	def setUP(self):	
		Multa.objetcs.create( titulo="teste de titulo multa")
		Usuario.objects.create(nome="teste nome usuario")
	def testeBD(self):
		self.assertEquals(User.objects.count(), 0)
		self.assertEquals(Usuario.objects.count(), 0)
		self.assertEquals(Multa.objects.count(), 0)