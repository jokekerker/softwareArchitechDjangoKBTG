from .settings import *

DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'mysite.urls'

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'softwareArcihtechDB',
        'USER': 'db_user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '54320',
    }
}

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}