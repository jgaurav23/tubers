import os

env =  os.environ.get('DJANGO_ENV', 'local')

if env == 'production':
    from .prod import *
else:
    from .local import *