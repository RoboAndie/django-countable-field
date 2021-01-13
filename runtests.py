import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

settings.configure(
    DEBUG=True,
    SECRET_KEY='fake-key',
    INSTALLED_APPS=(
        'tests',
        'countable_field'
    ),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
        }
    }
)

if hasattr(django, 'setup'):
    django.setup()

test_runner = DiscoverRunner(verbosity=1)

failures = test_runner.run_tests(['tests', ])

if failures:
    sys.exit(failures)
