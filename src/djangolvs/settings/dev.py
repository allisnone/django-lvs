# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from base import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
PROJECT_APPS = ('ipvsstat','ipvsadmin',);


INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#IP_VS_FILE = '../unittest/resource/ip_vs_2'
#IP_VS_STAT_FILE = '../unittest/resource/ip_vs_stats'
#IPVSADMIN = '../unittest/python/ipvsadmin.py'

