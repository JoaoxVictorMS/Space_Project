from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Renomeação de 'usuarios' para 'apps.usuarios' pois criei a pasta de apps, mudança de referência
    name = 'apps.usuarios'
