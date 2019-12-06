from .settings import *

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'mysite.urls'

INSTALLED_APPS += [
    'debug_toolbar',
]

POSTGRES_HOST = os.environ.setdefault('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.environ.setdefault('POSTGRES_PORT', '54320')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'softwareArcihtechDB',
        'USER': 'db_user',
        'PASSWORD': 'password',
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}