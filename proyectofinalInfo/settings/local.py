from .base import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'memoriasdenuestropueblo2',
        'USER': 'Tester', 
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
    }
}