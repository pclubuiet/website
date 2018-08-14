# These are the production settings. Particularly for heroku. At least for now.
# It is recommended that you don't touch these.

from .settings import *

Debug = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME', 'pclubuietdb'),
        'USER': os.getenv('DB_USER', 'pclubuietdb'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'pclubuietdb'),
        'HOST': os.getenv('DB_HOST', 'pclubuietdb'),
        'PORT': 5432,
    }
}

DATABASES['default'].update(dj_database_url.config(conn_max_age=500))
