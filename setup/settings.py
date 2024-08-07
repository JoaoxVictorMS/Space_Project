"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path, os
# dotenv é um módulo usado para criar e gerenciar as variáveis de ambiente
# Deste mesmo módulo, importe a função load_dotenv para carregar as variáveis de ambiente, assim sendo possível trabalhar com elas
from dotenv import load_dotenv

# Carrega as varáveis de ambiente, chamando a função importada
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Deve ser uma string, por isso a função str
# Quando esta aplicação for enviada ao github, não aparecerá a chave completa, apenas o que está escrito abaixo
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# Uma aplicação django possui vários apps, que são basicamente as funcionalidades da mesma.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Boa prática:
    # Colocando desta forma, o Django não irá apenas trazer o app de galeria, mas também o arquivo de configurações, apps.py, juntamente com todas as suas configurações. 
    # Em ambas as aplicações abaixo, galeria e usuario, possuem um arquivo chamado apps.py. Nele está contido uma classe com as configurações das respectivas aplicações, logo, tal classe será importada através do caminho especificado abaixo.
    # Foi colocado um apps. no inicio do app de galeria e de usuarios pois criei a pasta apps, mudança de referência    
    'apps.galeria.apps.GaleriaConfig',
    'apps.usuarios.apps.UsuariosConfig',
    # Adição do app de storages referente ao django-storages para a configuração do AWS S3
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS faz referência ao local onde os arquivos html estarão
        # BASE_DIR refere-se ao escopo principal do projeto, diretório raiz
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/



LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# ***** Variáveis globais para a configuração da AWS (BÁSICAS) *****

# Chave de acesso criada na página do usuário selecionado (django-dev) na opção IAM Identity and Access Management 
AWS_ACCESS_KEY_ID = str(os.getenv('AWS_ACCESS_KEY_ID'))

# Chave de acesso SECRETA criada na página do usuário selecionado (django-dev) na opção IAM Identity and Access Management 
AWS_SECRET_ACCESS_KEY = str(os.getenv('AWS_SECRET_ACCESS_KEY'))

# Nome do bucket criado
AWS_STORAGE_BUCKET_NAME = str(os.getenv('AWS_STORAGE_BUCKET_NAME'))

# Dominío do S3. Foi passado o nome do bukect + o segmento padrão 
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.sa-east-1.amazonaws.com' # Segmento padrão

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl' : 'max-age=86400'
}

# Pasta static
AWS_LOCATION = 'static'

AWS_QUERYSTRING_AUTH = False

AWS_HEADERS = {
    'Access-Control-Allow-Origin' : '*',
}

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": str(os.getenv('AWS_ACCESS_KEY_ID')),
            "secret_key": str(os.getenv('AWS_SECRET_ACCESS_KEY')),
            "bucket_name": str(os.getenv('AWS_STORAGE_BUCKET_NAME'))
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": str(os.getenv('AWS_ACCESS_KEY_ID')),
            "secret_key": str(os.getenv('AWS_SECRET_ACCESS_KEY')),
            "bucket_name": str(os.getenv('AWS_STORAGE_BUCKET_NAME'))
        },
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Variável global que armazena a url da pasta static
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

# O diretório dos arquivos estáticos da aplicação esta expecificado abaixo
# É necessário criar esta variável
# Foi criada um pasta chamado 'static' dentro da pasta setup. Nele que será acessado os arquivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static'),
]

# Informa a RAIZ, o diretório absoluto, dos arquivos, onde o Python irá coletar as arquivos estáticos e fazer as implementações e maipulações de onde estão os arquivos estáticos 
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Referências para o diretório responsável pelos arquivos de MÍDIA da aplicação.
# Graças a eles é possível fazer upload de arquivos, no caso imagens, para a aplicação
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# O trecho de código abaixo esta destinado as tags das messages
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success',
}