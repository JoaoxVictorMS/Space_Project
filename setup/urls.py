from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Todas as possíveis urls que serão atendidas na aplicação
urlpatterns = [
    path('admin/', admin.site.urls),
    # Quando chegar uma rota na raiz da aplicação, por isso as aspas vazias, será respondida com o index
    # A estrutura abaixo faz com que esta urlpatterns não precise mais listar cada página do app galeria
    # Agora será buscada todas as urls da aplicação de galeria
    # Renomeação de 'galeria.urls' para 'apps.galeria.urls' pois criei a pasta de apps, mudança de referência
    path('', include('apps.galeria.urls')),
    # Agora será buscada todas as urls da aplicação de usuarios
    # Renomeação de 'usuarios.urls' para 'apps.usuarios.urls' pois criei a pasta de apps, mudança de referência
    path('', include("apps.usuarios.urls")),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) -> Retirado daqui pois será adcionado no if abaixo

# BOA PRÁTICA:
# Caso a aplicação (settings) esteja em modo DEBUG , isto é, em funcionamento...
if settings.DEBUG:
    # Será adicionado, em urlpatterns, os static abaixo
    # A estrutura abaixo indica que o Django deve usar as referências MEDIA_URL e MEDIA_ROOT
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
