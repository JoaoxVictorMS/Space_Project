#  Cria secret keys aleatórias
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())