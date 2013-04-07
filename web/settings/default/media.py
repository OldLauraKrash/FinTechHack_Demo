# -*- coding: utf-8 -*-
import os
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

ATTACHMENT_ROOT = ''

# Must be more specific to the environment.

#STATIC_ROOT = os.path.abspath(os.path.join(APP_ROOT, 'static'))
#STATICFILES_DIRS = (
#        os.path.abspath(os.path.join(APP_ROOT, 'static')),
#    )
#MEDIA_ROOT = os.path.abspath(os.path.join(APP_ROOT, 'static'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"

#STATIC_ROOT = "/home/manav/workspace/manav/web/static"
#STATICFILES_DIRS = (
#    "/home/manav/workspace/manav/web/static",
#)

#MEDIA_URL = '/static/'
#STATIC_URL = '/static/'
#STATIC_DOC_ROOT = APP_ROOT + STATIC_URL

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".

STATIC_ROOT = os.path.abspath(os.path.join(APP_ROOT, 'static'))
STATICFILES_DIRS = (
        os.path.abspath(os.path.join(APP_ROOT, 'prestatic')),
    )
#MEDIA_ROOT = os.path.abspath(os.path.join(APP_ROOT, 'static'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"

#MEDIA_URL = '/static/'
STATIC_URL = '/static/'
STATIC_DOC_ROOT = APP_ROOT + STATIC_URL
