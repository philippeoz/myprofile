from decouple import config
 
from .base import BASE_DIR, DEBUG
 
 
# Urls para servir arquivos de mídia e estáticos
MEDIA_URL = config('MEDIA_URL', default='/media/')
STATIC_URL = config('STATIC_URL', default='/static/')
 
 
# Diretório para salvar arquivos de mídia e arquivos estáticos
STATIC_ROOT = BASE_DIR.child('frontend', 'staticfiles')
MEDIA_ROOT = BASE_DIR.child('media')

STATICFILES_DIRS = [
    BASE_DIR.child('frontend', 'static'),
]
 
# Engines para encontrar arquios estáticos
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
 
# Processadores e 'finders' para templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('frontend', 'templates'),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]