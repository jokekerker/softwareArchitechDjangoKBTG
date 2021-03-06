from .settings import *

DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0","54.255.131.153"]

ROOT_URLCONF = 'mysite.urls'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

POSTGRES_HOST = os.environ.setdefault('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.environ.setdefault('POSTGRES_PORT', '54320')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'softwarearcihtechdb',
        'USER': 'db_user',
        'PASSWORD': 'password',
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        '': {  # 'catch all' loggers by referencing it with the empty string
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True