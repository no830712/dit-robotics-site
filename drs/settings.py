"""
Django settings for drs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '#t@975wj5+af$dnbcr8*$ppn5=67*az3-g5j5-jf)uu)-2n%@4'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# TEMPLATE_DEBUG = DEBUG

# import security stuff from another untracked file
from .secret_settings import SECRET_KEY, DEBUG, TEMPLATE_DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'social.apps.django_app.default',
    'bootstrap3',
    'generic',
    'drs',
    'common',
    'accounts',
    'drive',
    'message_board',
    'bootstrap_plugin',
    'nthucourses',
    'dpcstatus',
    'projects',
    'printer_schedule',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
)

# allow templates to access the request object
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

ROOT_URLCONF = 'drs.urls'

WSGI_APPLICATION = 'drs.wsgi.application'

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply.ditrobotics@gmail.com'
from .secret_settings import EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'drs',
        'USER': 'drs',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True

from django.utils.timezone import timedelta
SESSION_COOKIE_AGE = timedelta(days=1) // timedelta(seconds=1)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

FILE_UPLOAD_TEMP_DIR = os.path.join(MEDIA_ROOT, 'tmp')

# a tuple that lists people who get code error notifications.
ADMINS = (('afg984', 'afg984@gmail.com'),)

# bootstrap3 settings

BOOTSTRAP3 = {
    'horizontal_field_class': 'col-md-8',
}

# Social Auth

SOCIAL_AUTH_FACEBOOK_KEY = '1557775327816367'
from drs.secret_settings import SOCIAL_AUTH_FACEBOOK_SECRET

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
)

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
