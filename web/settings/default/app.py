# -*- coding: utf-8 -*-
import os

LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../logs'))

LOGIN_MESSAGE = ""

DEBUG = False
TEMPLATE_DEBUG = DEBUG
APPEND_SLASH = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SERVER_EMAIL = ''
ADMINS = (
    ('test', 'test@abcd.com'),
)

MANAGERS = ADMINS
INTERNAL_IPS = '127.0.0.1'
SECRET_KEY = '(7+&u@tvzs01x73e6l5e5kq8(#irx7xf85ncb%hffvm)tyo$42'

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    #'pipeline.middleware.MinifyHTMLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'linaro_django_pagination.middleware.PaginationMiddleware',
    #'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'urls'

SITE_ID = 1

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend', )

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

LOGOUT_URL = '/accounts/logout/'
LOGIN_URL = '/accounts/login/'

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#DEFAULT_FROM_EMAIL = 'fastip_admin@ast1.com'
#EMAIL_HOST = 'smtp.exg6.exghost.com'
#EMAIL_HOST_USER = 'fastip_admin@ast1.com'
#EMAIL_HOST_PASSWORD = 'gZ4DD23@3e7'
#EMAIL_PORT = 2525
#EMAIL_USE_TLS = True

MIME_TYPE_ZIP = 'application/zip'
MIME_TYPE_CSV = 'text/csv'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s %(asctime)s %(module)s %(process)d] %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'verbose',
            'filename': LOG_DIR + '/fAST-ip-debug.log',
        },
        'socketlog': {
            'level': 'ERROR',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'verbose',
            'address': '/dev/log',
            'facility': 'local1',
        },
        'errorlog': {
            'level': 'ERROR',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'verbose',
            'filename': LOG_DIR + '/fAST-ip-error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers':['console', 'errorlog', 'socketlog'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.request': {
            'handlers': ['mail_admins', 'socketlog'],
            'level': 'ERROR',
            'propagate': True,
        },
        '': {
            'handlers': ['console', 'logfile', 'socketlog'],
            'level': 'DEBUG',
        },
    },
}
