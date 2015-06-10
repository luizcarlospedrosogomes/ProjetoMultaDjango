from django import forms

from multa.controleUsuario.models import Usuario
from multa.controleUsuario.models import Multa

class FormCadastro(forms.ModelForm):
	class Meta:
		model = Usuario
	
class FormCadastroMulta(forms.ModelForm):
	class Meta:
		model = Multa