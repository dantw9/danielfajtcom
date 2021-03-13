"""
WSGI config for danielfajtcom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
import env
from django.core.wsgi import get_wsgi_application

if env.PROJECT_PATH not in sys.path:
    sys.path.insert(0, '/opt/bitnami/projects/danielfajtcom')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'danielfajtcom.settings')

application = get_wsgi_application()
