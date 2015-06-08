from django import forms

class FormCadastro(forms.Form):
	nome = forms.CharField(max_length=100)
	cpf	= forms.CharField()
	