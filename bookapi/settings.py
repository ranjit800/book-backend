import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Secret key from environment (fallback for local dev)
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-dev-secret')

# ✅ DEBUG toggle via environment
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# ✅ Allowed hosts: Local + Render backend
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "10.0.2.2",
    "book-backend-hk0w.onrender.com",  # ✅ Exact backend Render domain
]

# ✅ Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'books',
    'corsheaders',
]

# ✅ Middleware: corsheaders first
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookapi.wsgi.application'

# ✅ SQLite for now
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Static files
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ CORS allowed origins: localhost + Netlify
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8081",  # Web dev via Expo
    "https://mypustak-book-app.netlify.app",  # ✅ Deployed frontend
]
