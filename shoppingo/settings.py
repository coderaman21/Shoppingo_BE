"""
Django settings for shoppingo project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY','')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG',False)

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "usermgmt.User"
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usermgmt',
    'home',
    'order',
    'payment',
    
    'django_extensions',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
     "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shoppingo.urls'

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

WSGI_APPLICATION = 'shoppingo.wsgi.application'


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'stock_price'),
)
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticatedOrReadOnly",),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
    
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=int(os.environ.get('ACCESS_TOKEN_LIFETIME',1))),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(os.environ.get('REFRESH_TOKEN_LIFETIME',1))),
}



CORS_ALLOWED_ORIGINS = [

    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1']

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
        'TIMEOUT':10800 # 3 hours
    }
}

FE_DOMAIN = os.environ.get('FE_DOMAIN','http://localhost:8000')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=os.environ.get('EMAIL_HOST','')
EMAIL_PORT=os.environ.get('EMAIL_PORT','')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER','')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD','')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL','')


RAZORPAY_KEY_ID = os.environ.get('RAZORPAY_KEY_ID','')
RAZORPAY_KEY_SECRET = os.environ.get('RAZORPAY_KEY_SECRET','')

LOGFILES_DIRECTORY_NAME = 'log_files'

if not os.path.exists(LOGFILES_DIRECTORY_NAME):
    os.makedirs(LOGFILES_DIRECTORY_NAME)

LOGGING = {  
    'version': 1,  
    # Version of logging  
    'disable_existing_loggers': False,  
    'formatters': {
        'default': {
            'format': '%(asctime)s  %(levelname)s %(pathname)s ln. no. %(lineno)d %(message)s',
        }
    },
    # Handlers ####
    'handlers': {  
        'warning_file': {  
            'level': 'WARNING',  
            'class': 'logging.FileHandler',  
            'filename': f'{LOGFILES_DIRECTORY_NAME}/warning.log',
            'formatter': 'default'    
        },
        'info_file': {  
            'level': 'INFO',  
            'class': 'logging.FileHandler',  
            'filename': f'{LOGFILES_DIRECTORY_NAME}/info.log',
            'formatter': 'default'    
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default'  
        },
    },  
    # Loggers ####  
    'loggers': {  
        'django': {  
            'handlers': ['warning_file','info_file','console'],  
            'level': 'DEBUG',  
            'propagate': True,  
            'level': os.environ.get('DJANGO_LOG_LEVEL', 'DEBUG')  
        },  
    },  
}  
import logging 
logger = logging.getLogger('django')