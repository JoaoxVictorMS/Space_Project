# ARQUIVO DESTINADO AS CONFIGURAÇÕES DO SITE DE ADMIN DO DJANGO

from django.contrib import admin
# # Renomeação de 'galeria.models' para 'apps.galeria.models' pois criei a pasta de apps, mudança de referência
from apps.galeria.models import Fotografia



class ListandoFotografias(admin.ModelAdmin):
    ''' Muda como as fotografias são listadas '''

    # As fotografias serão listadas apenas com as informações abaixo.
    list_display = ("id", "nome", "legenda", "publicada")

    # Quando clicarmos no nome da imagem, aparecera todas as suas informações, não precisando clicar apenas no ID.
    list_display_links = ("id", "nome")

    # Adiciona um campo de busca. DEVE SER UMA TUPLA E NÂO APENAS UM ITEM.
    search_fields = ("nome",)

    # Adicona um campo de filtro. Filtra pela categoria ou pelo usuario, ou os dois.
    list_filter = ("categoria", "usuario",)

    # Número de itens que aparecerão por página.
    list_per_page = 10

    # Agora é possíevel tornar um item publicado sem precisar clicar no item e fazer tal alteração
    list_editable = ("publicada",)



# Registrando o modelo de Fotografia dentro do site de admin.
# As classes são os parâmetros dessa função toda.
admin.site.register(Fotografia, ListandoFotografias)


