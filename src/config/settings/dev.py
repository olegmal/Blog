from config.settings.base import *  # NOQA

SECRET_KEY = "django-secret-key"
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}
#
# STATIC_URL = "static/"
# STATICFILES_DIRS = [BASE_DIR / "static"]
