#-*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from multa.controleUsuario.models import Usuario
from multa.controleUsuario.forms import FormCadastro
# Create your views here.
def index(request):
	return HttpResponse(u"Ola Mundo")

def cadastro(request):
	usuario_lista = Usuario.objects.all()
	return render_to_response('cadastroUsuario.html', {'usuario_lista': usuario_lista})

def adiciona(request):
	form = FormCadastro()
	return render_to_response("UsuarioAdiciona.html", {'form': form},
	context_instance=RequestContext(request))