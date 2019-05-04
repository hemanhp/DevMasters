"""
WSGI config for masters project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get('APP_ENV', 'development')
setting_path = 'masters.envs.' + env
os.environ["DJANGO_SETTINGS_MODULE"] = setting_path

application = get_wsgi_application()
