from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  
   (r'^$', "multa.controleUsuario.views.index"),
   (r'^cadastro/$', "multa.controleUsuario.views.cadastro"),
   (r'^cadastro/usuario/$', "multa.controleUsuario.views.adiciona"),
   (r'^cadastro/multa/$', "multa.controleUsuario.views.adicionaMulta"),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
