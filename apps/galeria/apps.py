from django.apps import AppConfig

# ARQUIVO DESTINADO AS CONFIGURAÇÕES ESPECÍFICAS DESTA APLICAÇÃO, A GALERIA
class GaleriaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Renomeação de 'galeria' para 'apps.galeria' pois criei a pasta de apps, mudança de referência 
    name = 'apps.galeria'
