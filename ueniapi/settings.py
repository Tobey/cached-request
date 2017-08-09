import os
import sys
import  logging

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#        REQUEST SETTINGS

REQUEST_URI  = os.getenv('UENI_REQUEST_URI', None) or 'http://localhost:8080/'
X_UENI_TOKEN = os.getenv('X_UENI_TOKEN', None)
USER_AGENT = 'Client-Library-1.0'

CACHE_REQUESTS = False
CACHE_EXPIRES = (7 * 24 * 3600)
                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#        OVERRIDE SETTINGS
CONFIG_OVERRIDE = 'uenihttp_settings.py'
cwd = os.getcwd()
if CONFIG_OVERRIDE in next(os.walk(cwd))[2]:
    sys.path.insert(0, cwd)
    logging.info('Overriding local configuration')
    from uenihttp_settings import *
    sys.path.pop(0)
                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
