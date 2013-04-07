#!/usr/bin/python
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
    import settings  # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("""Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.
You'll have to run django-admin.py, passing it your settings module.
(If the file settings.py does indeed exist, it's causing an ImportError somehow.)
"""
                     % __file__)
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) > 1:
        command = sys.argv[1]

    if  (command == 'runserver' or command == 'testserver'):

        # Make pydev debugger works for auto reload.

        try:
            import pydevd
        except ImportError:
            sys.stderr.write('Error: ' + 'You must add org.python.pydev.debug.pysrc to your PYTHONPATH.')
            sys.exit(1)

        from django.utils import autoreload
        m = autoreload.main


        def main(main_func, args=None, kwargs=None):

            if os.environ.get('RUN_MAIN') == 'true':

                def pydevdDecorator(func):

                    def wrap(*args, **kws):
                        pydevd.settrace(suspend=False, port=5678)
                        return func(*args, **kws)

                    return wrap

                main_func = pydevdDecorator(main_func)

            return m(main_func, args, kwargs)


        autoreload.main = main
    execute_manager(settings)
