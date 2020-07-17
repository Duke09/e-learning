from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = (
    ('Debopriyo Das', 'debopriyo09@gmail.com'),
)

ALLOWED_HOSTS =['*']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educa',
    }
}