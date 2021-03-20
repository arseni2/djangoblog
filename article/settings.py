"""
Django settings for article project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
django_heroku.settings(locals())
ALLOWED_HOSTS = ['*']
DEFAULT_CHARSET = 'UTF-8'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'waw^$+yuzrfw)o%w&(j*#2@h_#8xhqw$^+gs(+h==cp!kjru$*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Application definition

INSTALLED_APPS = [
    'blogapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'bootstrap4',
    'crispy_forms',
    

]

AUTH_USER_MODEL = 'blogapp.CustomUser'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
mail_key = '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'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ROOT_URLCONF = 'article.urls'
TEMPLATES = [
 {
   'BACKEND': 'django.template.backends.jinja2.Jinja2',
   'DIRS': [os.path.join(BASE_DIR, 'templates')],
   'APP_DIRS': True,
   'OPTIONS': {
     'environment': 'blogapp.jinja2.environment'
   },
 },
 {
   'BACKEND': 'django.template.backends.django.DjangoTemplates',
   'DIRS': [],
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

WSGI_APPLICATION = 'article.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'home'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = 'arsenij633@gmail.com'
EMAIL_HOST_PASSWORD = 'qwerty123098+'
#EMAIL_PORT = 465
#EMAIL_USE_SSL = True
#EMAIL_USE_TSL = False
EMAIL_PORT = 587
EMAIL_USE_TLS = True
