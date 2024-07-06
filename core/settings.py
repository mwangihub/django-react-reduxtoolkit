# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
from user.auth_config import *


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ["*"]

ROOT_URLCONF = "core.urls"

WSGI_APPLICATION = "core.wsgi.application"

# Security

CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Strict"
# Production CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "ckeditor",
    "django_countries",
    "phonenumber_field",
    "gmailapi_backend",
    "user",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]


def debug_folder(x):
    if DEBUG:
        return x
    return []


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "web/templates"),
            debug_folder(os.path.join(BASE_DIR, "web/test/build")),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATICFILES_DIRS = [BASE_DIR, "web/static"]
if DEBUG:
    STATICFILES_DIRS += [
        BASE_DIR,
        "web/test/src/vendor",
        BASE_DIR,
        "web/react/dist/assets",
    ]
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "static"


MEDIA_ROOT = BASE_DIR / "media"
INSTALLED_APPS += AUTH_INSTALLED_APPS
MIDDLEWARE += CORS_MIDDLEWARE
TEMPLATES[0]["OPTIONS"]["context_processors"] += CONTEXT_PROCESSORS
STATICFILES_DIRS += AUTH_STATIC
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
EMAIL_BACKEND = "gmailapi_backend.mail.GmailBackend"
GMAIL_API_CLIENT_ID = os.environ.get("GMAIL_CLIENT_ID")
GMAIL_API_CLIENT_SECRET = os.environ.get("GMAIL_CLIENT_SECRET")
GMAIL_API_REFRESH_TOKEN = os.environ.get("GMAIL_REFRESH_TOKEN")
ALLOWED_EMAIL = os.environ.get("ALLOWED_EMAIL").split(",")
