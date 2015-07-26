from .base import *  # noqa


INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
    'template_debug',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
) + MIDDLEWARE_CLASSES

# https://github.com/calebsmith/django-template-debug
TEMPLATE_DEBUG = True
