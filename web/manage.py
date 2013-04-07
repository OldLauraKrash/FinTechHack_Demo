#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
SYS_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))


sys.path += [
    #os.path.abspath(os.path.join(SYS_ROOT, 'lib/external')),
    #os.path.abspath(os.path.join(SYS_ROOT, 'lib/internal')),
    os.path.abspath(os.path.join(SYS_ROOT, 'src')),
]

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.local'

from django.core.management import execute_manager
try:
    import settings.local  # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write(
            """
            Error: Can't find the file 'settings.py' in the directory containing %r. 
            It appears you've customized things.
            You'll have to run django-admin.py, passing it your settings module.
            (If the file settings.py does indeed exist, it's causing an ImportError somehow.)
            """ % __file__ 
        )
    sys.exit(1)

if __name__ == '__main__':
    execute_manager(settings.local)
