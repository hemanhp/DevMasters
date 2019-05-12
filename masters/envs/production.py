from .common import *

DEBUG = False
ALLOWED_HOSTS = ['devmasters.ir']

STATICFILES_DIRS = [
    PROJECT_DIR + '/masters/statics'
]

STATIC_URL = '/static/'
STATIC_ROOT = "/avat/public/devmasters.ir/static/"
MEDIA_URL = '/media/'
MEDIA_ROOT = "/avat/public/devmasters.ir/media/"
