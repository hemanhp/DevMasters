from .common import *

DEBUG = False
ALLOWED_HOSTS = ['devmasters.ir']

STATICFILES_DIRS = [
    PROJECT_DIR + '/masters/statics'
]

STATIC_URL = '/static/'
STATIC_ROOT = "/avat/public/devmaster.ir/static/"


