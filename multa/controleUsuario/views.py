#-*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext

from multa.controleUsuario.models import Usuario
from multa.controleUsuario.models import Multa
from multa.controleUsuario.forms import FormCadastro
from multa.controleUsuario.forms import FormCadastroMulta


def index(request):
	return render_to_response('base.html', {})

def cadastro(request):
	multa_lista = Multa.objects.all()
	usuario_lista = Usuario.objects.all()
	return render_to_response('cadastroUsuario.html', {'usuario_lista': usuario_lista, 'multa_lista': multa_lista})

def adiciona(request):
	if request.method == "POST":
		form = FormCadastro(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormCadastro()
		return render_to_response("UsuarioAdiciona.html", {'form': form},
		context_instance=RequestContext(request))

def adicionaMulta(request):
	if request.method =="POST":
		form = FormCadastroMulta(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormCadastroMulta()
		return render_to_response("adicionaMulta.html", {'form': form},
		context_instance=RequestContext(request))
		
def editarUsuario(request, nr_id):
	usuarioID = get_object_or_404(Usuario, pk=nr_id)
	if request.method == "POST":
		form = FormCadastroMulta(request.POST, request.FILES, instance=usuarioID)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormCadastro(instance=usuarioID)
		return render_to_response("editar.html", {'form': form},
		context_instance=RequestContext(request))
	