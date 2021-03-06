"""
Django settings for ccrh_case_history project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yxmig_j9ncg00=%k%4_mj9j=k2vr5-+27sxqwfsms+$fphzhs$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ccrhch.azurewebsites.net']
INTERNAL_IPS = ['127.0.0.1']
SITE_ID = 1
ADMIN_EMAIL = 'smtp@baryonssoftsolutions.com'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'debug_toolbar',
    'import_export',
    'admin_reorder',
    'rest_framework',
    'rest_framework.authtoken',
    'master',
    'case_history',
    'user_profile',
    'roles_permissions',
    'utils',
    'notifications',
    'ckeditor',
    'nested_inline',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'audit_log.middleware.UserLoggingMiddleware',
]

ROOT_URLCONF = 'ccrh_case_history.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'ccrh_case_history.wsgi.application'
#Media Configurations
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE" : 'djongo',
#         "ENFORCE_SCHEMA": True,
#         "NAME": 'ccrh',
#         "HOST": 'localhost',
#         "PORT" : 27017,
#         "USERNAME": 'root',
#         "PASSWORD": 'mongodb',
#         "AUTH_SOURCE": 'ccrh',
#         "AUTH_MECHANISM": 'SCRAM-SHA-1',
#     },
# }
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propogate': False,                        
                }
            },
         },
        'NAME': 'ccrhmongo',
        'CLIENT': {
            'host': 'mongodbccrh.mongo.cosmos.azure.com',
            'port': 10255,
            'username': 'ccrhmongo',
            'password': 'pbK6PfiZVWNvpM9cVkkYjxm1jSqSygPrf4Ephvh3QyDFRydgdSV5RtYeBjyQW9H7gXe8paWW5Nd6LIPFmpY7LQ==',
            'authSource': 'admin',
            'authMechanism': 'SCRAM-SHA-1'
        }
    }
}
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LANGUAGES = (
    ('en', _('English')),
#     ('hi', _('Hindi')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

AUTHENTICATION_BACKENDS = (
    'user_profile.email_auth.EmailAuthBackend',
)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'sg3plcpnl0228.prod.sin3.secureserver.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'smtp@baryonssoftsolutions.com'
EMAIL_HOST_PASSWORD = 'Baryons@123456'
DEFAULT_FROM_EMAIL = 'smtp@baryonssoftsolutions.com'
SEND_MAIL_ALL_PLACE = True

'''Email setting Ends'''

'''Notification Settings - Starts '''
SEND_NOTIFICATIONS_ALL_PLACE = True
DJANGO_NOTIFICATIONS_CONFIG = {'SOFT_DELETE': True} #For changing the flag if deleted

'''Default email sending for approval status'''
ADMIN_REGISTRATION_EMAIL = "ccrhadmin@admin.com"

'''Rest Framework Setting Start Here'''
REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': [
       'rest_framework.authentication.TokenAuthentication',
   ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
    ]
}
'''Rest Framework Setting End Here'''
#Setting below to false bcz db module doesn't support transaction
IMPORT_EXPORT_USE_TRANSACTIONS = False

CCRH_HOME_URL = 'https://ccrh.azurewebsites.net/en'
CCRH_LOGIN_URL = 'https://ccrh.azurewebsites.net/en/user/login'
LOGIN_ERROR_URL    = 'user_profile:login'
LOGIN_URL    = 'user_profile:login'
LOGOUT_REDIRECT_URL = 'https://ccrh.azurewebsites.net/en/'

