from .base import *



DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbi2c9j8ll5nm2',
        'USER': 'rqccimwdngxfzh',
        'PASSWORD': '3702d459e3788da74ad9f80b8e53c17f39f8eac428c2008e2c3366e14a91eac5',
        'HOST': 'ec2-184-73-198-174.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATICFILES_DIRS=(BASE_DIR,'/blog_dz/static')