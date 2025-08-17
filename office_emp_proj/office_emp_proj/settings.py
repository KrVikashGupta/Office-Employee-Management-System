from pathlib import Path
import os
<<<<<<< HEAD
import dj_database_url  # ✅ make sure this is installed

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
=======
import dj_database_url  # make sure this is in requirements.txt

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')

>>>>>>> origin/main
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']

<<<<<<< HEAD
# Application definition
=======
>>>>>>> origin/main
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'emp_app',   # your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
<<<<<<< HEAD
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ✅ must be here
=======
    'whitenoise.middleware.WhiteNoiseMiddleware',  # important for static files
>>>>>>> origin/main
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'office_emp_proj.urls'

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

WSGI_APPLICATION = 'office_emp_proj.wsgi.application'

<<<<<<< HEAD
# ✅ Database: Use Postgres in production, SQLite locally
=======
# ✅ Use Postgres if DATABASE_URL exists, else use SQLite
>>>>>>> origin/main
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ✅ Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

<<<<<<< HEAD
# Default primary key field type
=======
>>>>>>> origin/main
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
