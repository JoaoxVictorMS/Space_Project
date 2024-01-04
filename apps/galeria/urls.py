from django.urls import path
# ***** O ARQUIVO URLS.PY É UMA BOA PRÁTICA EM APLCIAÇÕES DJANGO, EMBORA SER NECESSÁRIO CRIALA *****
# Importe do arquivo 'views', contido no app 'galeria', a função index, imagem  assim por diante
# Todas essas importações se referem as páginas que serão devolvidas quando requisitadas (request) pelo usário
# Renomeação de 'galeria.views' para 'apps.galeria.views' pois criei a pasta de apps, mudança de referência
from apps.galeria.views import \
    index, imagem , buscar, nova_imagem, deletar_imagem, editar_imagem, filtro

urlpatterns = [
    # Quando chegar uma rota na raiz da aplicação, por isso as aspas vazias, será respondida com o index
    path('', index, name='index'),

    # Aqui o valor é recebido em imagem(no meio). 
    # Logo, foi passado através da estrutura <int:foto_id>, as informações da imagem, referenciadas pelo id da imagem que é um número, através da url.
    path ('imagem/<int:foto_id>', imagem, name='imagem'),

    # Rota para a aba de buscar
    path("buscar", buscar, name="buscar"),

    # Rota para a nova função de adicionar imagens 
    path("nova_imagem", nova_imagem, name='nova_imagem'),

    # Rota para a nova função de editar imagens  
    # Foi passado através da estrutura <int:foto_id>, as informações da imagem, referenciadas pelo id da imagem que é um número, através da url. 
    # Todas vez que o path de editar_imagem for solicitado, ele deve receber uma informação em  formato de int, que é o foto_id
    path("editar_imagem/<int:foto_id>", editar_imagem, name='editar_imagem'),

    # Rota para a nova função de deletar imagens
    path("deletar-imagem/<int:foto_id>", deletar_imagem, name='deletar_imagem'),

    # Rota para a função de filtragem de imagens, no caso aquelas tags de nebulosa, galáxia, estrela e planeta localizadas no index
    path("fitro/<str:categoria>", filtro, name='filtro'),
    ]