from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  
   (r'^$', "multa.controleUsuario.views.index"),
   (r'^cadastro/', "multa.controleUsuario.views.cadastro"),
   (r'^adiciona/$', "multa.controleUsuario.views.adiciona"),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
