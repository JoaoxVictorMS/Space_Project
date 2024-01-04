# ***** O ARQUIVO URLS.PY É UMA BOA PRÁTICA EM APLCIAÇÕES DJANGO, EMBORA SENDO NECESSÁRIO CRIALA *****
from django.urls import path
# Renomeação de 'usuarios.views' para 'apps.usuarios.views' pois criei a pasta de apps, mudança de referência
from apps.usuarios.views import login, cadastro, logout

urlpatterns = [
    # Caminhos que referenciam para as páginas de login, cadastro e logout
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    ]