from .base import *  # noqa

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
) + MIDDLEWARE_CLASSES

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
