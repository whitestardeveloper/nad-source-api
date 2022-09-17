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
import environ
import os
from datetime import timedelta
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
# ALLOWED_HOSTS = ['89.252.135.196', 'alldaynaturel.com', 'www.alldaynaturel.com', 'localhost', '*']
ALLOWED_HOSTS = ['89.252.135.196', 'alldaynaturel.com', 'www.alldaynaturel.com', 'localhost', '*']
CSRF_TRUSTED_ORIGINS = [
    'https://89.252.135.196', 
    'https://alldaynaturel.com', 
    'https://www.alldaynaturel.com', 
    'https://localhost',
    'http://89.252.135.196', 
    'http://alldaynaturel.com', 
    'http://www.alldaynaturel.com', 
    'http://localhost'
]
CORS_ALLOWED_ORIGINS = [
    'https://89.252.135.196', 
    'https://alldaynaturel.com', 
    'https://www.alldaynaturel.com', 
    'https://localhost:8000',
    'http://89.252.135.196', 
    'http://alldaynaturel.com', 
    'http://www.alldaynaturel.com', 
    'http://localhost:8000',
    'https://127.0.0.1:8000',
    'http://127.0.0.1:8000',
]

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
    'django.contrib.sites',
    'rest_framework_swagger',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.apple',
    'dj_rest_auth.registration',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django_filters',
    'django_firebase',
    'multiselectfield',
    'corsheaders',
    # 'cloudinary',
    'source',
]

SITE_ID = 1

REST_USE_JWT = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=365),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
    # 'ROTATE_REFRESH_TOKENS': False,
    # 'BLACKLIST_AFTER_ROTATION': False,
    # 'UPDATE_LAST_LOGIN': False,

    # 'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': SECRET_KEY,
    # 'VERIFYING_KEY': None,
    # 'AUDIENCE': None,
    # 'ISSUER': None,
    # 'JWK_URL': None,
    # 'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    # 'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    # 'USER_ID_FIELD': 'id',
    # 'USER_ID_CLAIM': 'user_id',
    # 'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM': 'token_type',
    # 'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    # 'JTI_CLAIM': 'jti',

    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
     "apple": {
        "APP": {
            # Your service identifier.
            "client_id":"com.localhost:8000.social-login-1234",
            # The Key ID (visible in the "View Key Details" page).
            "secret": "sociallogintest1234",
            "key": "ABCDEF",
            "certificate_key": """----BEGIN PRIVATE KEY----
KJASDHKASDHKASJHDASKJHDKJASHDHJA----END PRIVATE KEY----"""
        }
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False

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
            'libraries' : {
                'staticfiles': 'django.templatetags.static', 
            }
        },
    },
]

WSGI_APPLICATION = 'ws_source.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.postgresql_psycopg2'),
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
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
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
