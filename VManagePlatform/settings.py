"""
Django settings for VManagePlatform project.

Generated by 'django-admin startproject' using Django 1.8.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import djcelery
from celery import  platforms


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

''' celery config '''
djcelery.setup_loader()
BROKER_URL = 'redis://192.168.1.233:6379/0'
CELERY_RESULT_BACKEND = 'djcelery.backends.database.DatabaseBackend'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERYD_MAX_TASKS_PER_CHILD = 40
CELERY_TRACK_STARTED = True
CELERY_TIMEZONE='Asia/Shanghai'
platforms.C_FORCE_ROOT = True


'''on_vnc config'''
VNC_PROXY_PORT = 6080
VNC_TOKEN_PATH = os.path.join(os.getcwd(), 'vnc', 'utils', 'vnc_tokens')


LIBVIRT_KEEPALIVE_INTERVAL = 5
LIBVIRT_KEEPALIVE_COUNT    = 5

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nx-0=c6d*n8e_#c*f*=18!14ju$h%xvwbj6!q!yysgf#n*vmw1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'VManagePlatform',
    'rest_framework',
    'djcelery'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
#     'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
#     'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',
#     ),              
}

ROOT_URLCONF = 'VManagePlatform.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'VManagePlatform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'vmanage',
        'USER':'root',
        'PASSWORD':'welliam',
        'HOST':'192.168.1.201'
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
     'E:\\MyPros\\VManagePlatform\\VManagePlatform\\static\\',
    )
TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR,'mysite\templates'),
    'E:\\MyPros\\VManagePlatform\\VManagePlatform\\templates\\',
)


LOGIN_URL = '/login'