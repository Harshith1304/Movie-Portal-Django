from pathlib import Path
import os
# --- BASE DIRECTORY ---
BASE_DIR = Path(__file__).resolve().parent.parent


# --- SECURITY SETTINGS ---
SECRET_KEY = 'django-insecure-your-secret-key-here'  # Replace later with an env var in production
DEBUG = True

ALLOWED_HOSTS = []


# --- INSTALLED APPS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'crispy_forms',

    # Local apps
    'movies',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',   # Required for sessions
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for auth
    'django.contrib.messages.middleware.MessageMiddleware',     # Required for messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JS, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'movies' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # for collectstatic



# --- URL CONFIGURATION ---
ROOT_URLCONF = 'movieportal.urls'


# --- TEMPLATES CONFIGURATION ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],      # Main templates folder
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


# --- WSGI CONFIGURATION ---
WSGI_APPLICATION = 'movieportal.wsgi.application'


# --- DATABASE CONFIGURATION (PostgreSQL) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movie_db',           # Change if needed
        'USER': 'movie_user',         # Change to your PostgreSQL username
        'PASSWORD': '@Harshith13',  # Change to your PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# --- PASSWORD VALIDATION ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- INTERNATIONALIZATION ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'   # You can change to your region if needed
USE_I18N = True
USE_TZ = True


# --- STATIC & MEDIA FILES ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'movies' / 'static']   # Create this folder next to manage.py
STATIC_ROOT = BASE_DIR / 'staticfiles'     # For collectstatic (deployment)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'     # For uploaded movie posters, etc.


# --- DEFAULT AUTO FIELD ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- LOGIN/LOGOUT REDIRECTS ---
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
