from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
  
   (r'^$', "multa.controleUsuario.views.index"),
   (r'^cadastro/$', "multa.controleUsuario.views.cadastro"),
   (r'^cadastro/usuario/$', "multa.controleUsuario.views.adiciona"),
   (r'^cadastro/multa/$', "multa.controleUsuario.views.adicionaMulta"),
   (r'^cadastro/usuario/editar/(?P<nr_id>\d+)/$', "multa.controleUsuario.views.editarUsuario"),
   (r'^cadastro/multa/editar/(?P<nr_id>\d+)/$', "multa.controleUsuario.views.editarMulta"),
   (r'^media/(?P<path>.*)$', "django.views.static.serve",{'document_root':settings.MEDIA_ROOT}),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
