# -*- coding: utf-8 -*-
from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Dev server email settings
# python -m smtpd -n -c DebuggingServer localhost:1025
MAIL_HOST = 'localhost'
EMAIL_PORT = 1025
