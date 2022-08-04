"""
Django settings for ws_source project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from email.policy import default
import dj_database_url
from pathlib import Path
import warnings
import environ, os
# import pyrebase
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import storage


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# cred = credentials.Certificate('../serviceAccountKey.json')
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'ws-source.appspot.com'
# })
# bucket = storage.bucket()
# default_storage = bucket

DEFAULT_FILE_STORAGE = 'django_firebase.storage.FirebaseStorage'
FIREBASE_STORAGE_BUCKET = 'ws-source.appspot.com'
FIREBASE_CERT_DATA = os.path.join(BASE_DIR, './serviceAccountKey.json')

# import firebase_admin
# from google.cloud import storage
# from firebase_admin import credentials
# from firebase_admin import storage
# import cloudinary

# firebase_config = {
#   "apiKey": "AIzaSyDcKdD0bqc7a-r9FKCFPiR5VJuo-S2zQks",
#   "authDomain": "ws-source.firebaseapp.com",
#   "projectId": "ws-source",
#   "storageBucket": "ws-source.appspot.com",
#   "messagingSenderId": "534098630740",
#   "appId": "1:534098630740:web:5f80472423b63f6b7175c1",
#   "measurementId": "G-EL3E5MTZ3R",
#   "databaseURL":""
# }

# firebase_storage = pyrebase.initialize_app(firebase_config)
# storage = firebase_storage.storage()



warnings.filterwarnings("ignore", message="No directory at", module="whitenoise.base" )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

env = environ.Env(DEBUG=(bool, False))

# reading .env file
environ.Env.read_env(env_file='{0}/.env'.format(BASE_DIR))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-nq5@o+af^xr7%f=s-c-@$omm096(%w+yemk(6#%tu63n&up4d8')
# SECRET_KEY = 'django-insecure-nq5@o+af^xr7%f=s-c-@$omm096(%w+yemk(6#%tu63n&up4d8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', default=False)

# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', default='*').split(',')
ALLOWED_HOSTS = ['93.115.79.32', 'alldaynaturel.com', 'www.alldaynaturel.com', 'localhost']
# cloudinary.config( 
#   cloud_name = "de0cqnzbt", 
#   api_key = "861677473894574", 
#   api_secret = "xGqQZXU-AEo8I93_xb1GIldZBlo" 
# )

# CLOUDINARY_URL=cloudinary://861677473894574:xGqQZXU-AEo8I93_xb1GIldZBlo@de0cqnzbt

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'django_firebase',
    'multiselectfield',
    # 'cloudinary',
    'source'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
      "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ws_source.urls'

TEMPLATES = [
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

WSGI_APPLICATION = 'ws_source.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', '5432'),
    }
}

DATABASE_URL = os.environ.get('DATABASE_URL')
db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500, ssl_require=False)
DATABASES['default'].update(db_from_env)


# DATABASES = {
#     'default': env.db(),
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'ws_source.custom.CustomPagination',
    'PAGE_SIZE': 20
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 35000 # higher than the count of fields

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
