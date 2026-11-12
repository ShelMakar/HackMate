__all__ = ()

import os
import pathlib

import django.urls
import django.utils.translation
import dotenv


dotenv.load_dotenv()


def check_boolean(value):
    return value.lower() in (
        "true",
        "1",
        "y",
        "yes",
    )


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", default="123456")

DEBUG = check_boolean(os.getenv("DJANGO_DEBUG", default="False"))

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(
    ",",
)

INSTALLED_APPS = [
    "homepage.apps.HomepageConfig",
    "users.apps.UsersConfig",
    "vacancies.apps.VacanciesConfig",
    "notify.apps.NotifyConfig",
    "api.apps.ApiConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_cleanup.apps.CleanupConfig",
    "star_ratings",
    "sorl.thumbnail",
    "tinymce",
    "notifications",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "users.middleware.ProxyUserMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

if DEBUG:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INTERNAL_IPS = ["127.0.0.1", "localhost"]

ROOT_URLCONF = "hackmate.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "hackmate.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "data" / "db.sqlite3",
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth"
            ".password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth" ".password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth"
            ".password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth"
            ".password_validation.NumericPasswordValidator"
        ),
    },
    {
        "NAME": "users.validators.MaxLengthPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"
LOCALE_PATHS = (BASE_DIR / "locale/",)
LANGUAGES = [
    ("ru", django.utils.translation.gettext_lazy("Русский")),
    ("en", django.utils.translation.gettext_lazy("English")),
]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static_dev",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = [
    "users.backends.EmailOrUsernameModelBackend",
    "django.contrib.auth.backends.ModelBackend",
]

DJANGO_MAIL = os.getenv("DJANGO_MAIL")

MAX_AUTH_ATTEMPTS = os.getenv("DJANGO_MAX_AUTH_ATTEMPS", 5)


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = os.getenv("EMAIL_HOST", "your_email_host")
EMAIL_PORT = os.getenv("EMAIL_PORT", "your_email_port")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "your_email")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "your_password")
EMAIL_USE_SSL = check_boolean(os.getenv("DJANGO_EMAIL_USE_SSL", "True"))

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

LOGIN_REDIRECT_URL = django.urls.reverse_lazy("homepage:homepage")
LOGIN_URL = django.urls.reverse_lazy("users:login")
LOGOUT_REDIRECT_URL = django.urls.reverse_lazy("users:login")


if DEBUG:
    DEFAULT_USER_IS_ACTIVE = check_boolean(
        os.getenv(
            "DJANGO_DEFAULT_USER_IS_ACTIVE",
            default="True",
        ),
    )

else:
    DEFAULT_USER_IS_ACTIVE = check_boolean(
        os.getenv(
            "DJANGO_DEFAULT_USER_IS_ACTIVE",
            default="False",
        ),
    )

DJANGO_NOTIFICATIONS_CONFIG = {
    "USE_JSONFIELD": True,
}

STAR_RATINGS_RERATE_SAME_DELETE = True

STAR_RATINGS_STAR_HEIGHT = 20
STAR_RATINGS_STAR_WIDTH = 20


MIGRATION_MODULES = {
    "star_ratings": "users.star_ratings_migrations",
}
