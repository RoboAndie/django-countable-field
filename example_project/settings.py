from django.conf.urls import url
from os.path import join, dirname, abspath

from example_project import views

DEBUG = True

SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__

urlpatterns = [
    url(r'^$', views.test_form_view),
]

INSTALLED_APPS = [
    'django.contrib.staticfiles',

    'crispy_forms',

    'example_project',
    'countable_field'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

BASE_DIR = dirname(dirname(abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, "templates")],
        'APP_DIRS': True,
    },
]

PROJECT_ROOT = dirname(abspath(__file__))
STATIC_ROOT = join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
