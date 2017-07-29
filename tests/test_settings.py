SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
    "countable_field"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}