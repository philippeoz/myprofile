from decouple import config
 
from dj_database_url import parse as db_url
 
from unipath import Path

# Diretório base do projeto
BASE_DIR = Path(__file__).ancestor(2)

DEBUG = config('DEBUG', default=False, cast=bool)

# Apps ativos
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 
    # Apps de terceiros
    # 'rest_framework',
    'bootstrap4',
 
    # Local apps
    'backend.core',
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

# Configurações de Url e GateWay
ROOT_URLCONF = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'

# Database
PROJECT_DB_URL = config('DATABASE_URL', cast=db_url)
DATABASES = {  
    'default': PROJECT_DB_URL if PROJECT_DB_URL else {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Internacionaização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_L10N = True
USE_TZ = False
USE_THOUSAND_SEPARATOR = True
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d')

# Configurações de Login
AUTH_USER_MODEL = 'core.Usuario'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = 'profile'