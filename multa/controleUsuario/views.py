#-*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from multa.controleUsuario.models import Usuario
from multa.controleUsuario.forms import FormCadastro
from multa.controleUsuario.forms import FormCadastroMulta


def index(request):
	return render_to_response('base.html', {})

def cadastro(request):
	usuario_lista = Usuario.objects.all()
	return render_to_response('cadastroUsuario.html', {'usuario_lista': usuario_lista})

def adiciona(request):
	if request.method == "POST":
		form = FormCadastro(request.POST, request.FILES)
		if form.is_valid():
			dados = form.cleaned_data
			item = Usuario(
							nome = dados['nome'],
							cpf = dados['cpf']
							)
			item.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormCadastro()
		return render_to_response("UsuarioAdiciona.html", {'form': form},
		context_instance=RequestContext(request))

def adicionaMulta(request):
	form = FormCadastroMulta()
	return render_to_response("adicionaMulta.html", {'form': form},
		context_instance=RequestContext(request))