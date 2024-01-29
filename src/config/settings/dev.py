import os

from config.settings.base import *  # NOQA

SECRET_KEY = "django-secret-key"
DEBUG = True

# INSTALLED_APPS = [   # NOQA
#     # "django_extensions",
# ]

ALLOWED_HOSTS = []

DATABASE_ROUTERS = ['core.utils.db_routers.NonRelRouter', ]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "0.0.0.0",
            "PORT": 5432,
        },
        "nonrel": {
            "ENGINE": "djongo",
            "NAME": os.environ.get('MONGO_DB_NAME'),
            "CLIENT": {
                "host": os.environ.get('MONGO_DB_HOST'),
                "port": int(os.environ.get('MONGO_DB_PORT')),
                "username": os.environ.get('MONGO_DB_USERNAME'),
                "password": os.environ.get('MONGO_DB_PASSWORD'),
                },
            }
        }

else:
    DATABASES = {
        # "default_postgres_local": {
        #     "ENGINE": "django.db.backends.postgresql",
        #     "NAME": "my_database",
        #     "USER": "oleg",
        #     "PASSWORD": "admin",
        #     "HOST": "localhost",
        #     "PORT": 5432,
        #      },
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",  # NOQA
        }
    }

# STATIC_URL = "static/"
# STATICFILES_DIRS = [BASE_DIR / "static"]
