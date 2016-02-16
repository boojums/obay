"""
Django settings for obay_project project.

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
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
EMAIL_USE_TLS = ''


# Fixtures
FIXTURE_PATH = os.path.join(BASE_DIR, 'fixtures')
FIXTURE_DIRS = (
    FIXTURE_PATH,
)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    'obay',

    'django_extensions',
    'registration',
    'sorl.thumbnail',
    'crispy_forms',
    'fluent_comments',
    'django_comments',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'obay_project.urls'

WSGI_APPLICATION = 'obay_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Registration settings
REGISTRATION_OPEN = True                # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/obay/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'  # The page users are directed to if they are not logged in,


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    STATIC_PATH,
)
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Template locations
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    )

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

# django-resized defaults
DJANGORESIZED_DEFAULT_SIZE = [640, 480]
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True

# crispy default template pack
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# SITE_ID must be defined for django_comments
SITE_ID = 1

# COMMENTS_APP required for fluent_comments
COMMENTS_APP = 'fluent_comments'
FLUENT_COMMENTS_EXCLUDE_FIELDS = ('email', 'url')

try:
    from local_settings import *
except:
    print """
    =======================================
    Missing local_settings.py file. Needed for email and database information.
    =======================================
    """
