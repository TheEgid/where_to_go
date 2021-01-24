from pathlib import Path
import platform
import osgeo
from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

OPERATING_SYSTEM = 'Linux' if (platform.system() != "Windows") else 'Windows'

# This paths Gdal and Geos settings for Windows only
# https://stackoverflow.com/questions/44140241/geodjango-on-windows-try-setting-gdal-library-path-in-your-settings
# https://code.djangoproject.com/ticket/28237
if platform.system() == "Windows":
    OSGEO_PATH = Path(''.join(osgeo.__path__))
    GDAL_LIBRARY_PATH = str(OSGEO_PATH / 'gdal301')
    GEOS_LIBRARY_PATH = str(OSGEO_PATH / 'geos_c')

SECRET_KEY = env.str("SECRET_KEY")

if OPERATING_SYSTEM != "Windows":
    DEBUG = False
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
else:
    DEBUG = env.bool("DEBUG", default=True)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'places',
    'tinymce',
    'adminsortable2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'where_to_go.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'where_to_go.wsgi.application'

DATABASES = {'default': {
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': 'database1',
    'USER': env.str("POSTGRES_USER"),
    'PASSWORD': env.str("POSTGRES_PASSWORD"),
    'PORT': '5432',
    'HOST': 'localhost' if (OPERATING_SYSTEM != 'Linux') else 'database1'}
}

SERIALIZATION_MODULES = {
    "geojson": "django.contrib.gis.serializers.geojson",
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

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_ROOT = BASE_DIR.parent / 'static'

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static', ]

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'
