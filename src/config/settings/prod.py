from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-1v#7rp20t^!^0o$0lud$8r&rlhrap^bjg7h@--(45-a+rdt$g8"
DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
