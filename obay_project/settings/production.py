# -*- coding: utf-8 -*-
from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Email settings
EMAIL_HOST = 'mail.boojumware.com'
EMAIL_HOST_USER = 'obay@boojumware.com'
EMAIL_HOST_PASSWORD = 'Pretzel5!'
EMAIL_PORT = '587'
EMAIL_USE_TLS = 'TRUE'

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
