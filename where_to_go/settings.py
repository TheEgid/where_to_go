from pathlib import Path
import platform
import os
import osgeo
from dotenv import load_dotenv

OPERATING_SYSTEM = 'Linux' if (platform.system() != "Windows") else 'Windows'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = BASE_DIR / '.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


if OPERATING_SYSTEM == 'Windows':
    OSGEO_PATH = Path(''.join(osgeo.__path__))
    GDAL_LIBRARY_PATH = str(OSGEO_PATH / 'gdal301')
    GEOS_LIBRARY_PATH = str(OSGEO_PATH / 'geos_c')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

if OPERATING_SYSTEM != "Windows":
    DEBUG = False
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
else:
    DEBUG = os.getenv("DEBUG", "true").lower() in ['yes', '1', 'true']

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'rest_framework_gis',
    'django.contrib.gis',
    'places',
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
    'USER': os.getenv("POSTGRES_USER1"),
    'PASSWORD': os.getenv("POSTGRES_PASSWORD1"),
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

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = BASE_DIR.parent / 'static'

STATIC_URL = '/static/'

STATICFILES_DIRS = (BASE_DIR / 'static',)

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# breakpoint()
