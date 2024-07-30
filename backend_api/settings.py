"""
Django settings for backend_api project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
import os
import dotenv
project_folder = os.getcwd()
xx =os.path.join(project_folder, '.env')
dotenv.load_dotenv(xx)

import pymysql
pymysql.install_as_MySQLdb()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#bx$ivmdn5a!p!a%n1c)58)uqck-yk!*oi2a*j$hdz762m77-)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

CORS_ORIGIN_ALLOW_ALL=True

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "Access-Control-Allow-Origin"
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'java_signatures.apps.JavaSignaturesConfig',
    'team2b.apps.Team2BConfig',
    'data_tracking',
    'django_redis',
    'corsheaders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'backend_api.urls'

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

WSGI_APPLICATION = 'backend_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

print(os.getenv('CLICKMANAGER_ENV_USER'))

DATABASES = {
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': os.getenv('DB_NAME'),  
        'USER': os.getenv('DB_USER'),  
        'PASSWORD': os.getenv('DB_PASS'),  
        'HOST': os.getenv('DB_HOST'),  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }, 
    'cm-env1': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'clickManager',  
        'USER': os.getenv('CLICKMANAGER_ENV_USER'),  
        'PASSWORD': os.getenv('CLICKMANAGER_ENV_USER_PASS'),  
        'HOST': os.getenv('CLICKMANAGER_ENV1_HOST'),  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }, 
    'cm-env2': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'clickManager',  
        'USER': os.getenv('CLICKMANAGER_ENV_USER'),  
        'PASSWORD': os.getenv('CLICKMANAGER_ENV_USER_PASS'),  
        'HOST': os.getenv('CLICKMANAGER_ENV2_HOST'),  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    },
    'cm-env3': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'clickManager',  
        'USER': os.getenv('CLICKMANAGER_ENV_USER'),  
        'PASSWORD': os.getenv('CLICKMANAGER_ENV_USER_PASS'),  
        'HOST': os.getenv('CLICKMANAGER_ENV3_HOST'),  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    },
    'at-env1': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'apptracking_api',  
        'USER': os.getenv('APPTRACKING_ENV_USER'),  
        'PASSWORD': os.getenv('APPTRACKING_ENV_USER_PASS'),  
        'HOST': os.getenv('APPTRACKING_ENV1_HOST'),  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    },
    'at-env2': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'apptracking_api',  
        'USER': os.getenv('APPTRACKING_ENV_USER'),  
        'PASSWORD': os.getenv('APPTRACKING_ENV_USER_PASS'),  
        'HOST': os.getenv('APPTRACKING_ENV2_HOST'),  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    },
    'at-env3': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'apptracking_api',  
        'USER': os.getenv('APPTRACKING_ENV_USER'),  
        'PASSWORD': os.getenv('APPTRACKING_ENV_USER_PASS'),  
        'HOST': os.getenv('APPTRACKING_ENV3_HOST'),  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    },
    
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SOCKET_TIMEOUT': 5,
            'SOCKET_CONNECT_TIMEOUT': 5,
        },
        "KEY_PREFIX": "team2b"

    }
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
