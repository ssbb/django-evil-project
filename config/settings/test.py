import logging

from .base import *  # noqa

DEBUG = False
TEMPLATE_DEBUG = False

TEST_RUNNER = 'rainbowtests.test.runner.RainbowDiscoverCoverageRunner'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db'
    }
}

CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
BROKER_BACKEND = 'memory'

EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

logging.disable(logging.CRITICAL)
