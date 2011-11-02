import os
here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PROJECT_ROOT = here('..')

root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

PROJECT_MODULE = '.'.join(__name__.split('.')[:-2])

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                            'interface.authentication.JnbAuthenticationBackend',)

JNB_WEBSERVICES_URL = 'http://127.0.0.1:8080/JnbWebServices'

MANAGERS = ADMINS

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': root('etc', 'development.db')                      # Or path to database file if using sqlite3.    }
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Santiago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-cl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = root('uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".

STATIC_ROOT = root('static', 'assets')
STATIC_URL = '/staticfiles/'

STATICFILES_DIRS = (
    root('staticfiles'),
)

ADMIN_MEDIA_PREFIX = '%sadmin/' % STATIC_URL

AUTH_PROFILE_MODULE = 'interface.UserProfile'

CARGOS_CUERPO = {
    'Comandante': 4,
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'djangoflash.context_processors.flash',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'djangoflash.middleware.FlashMiddleware',
)

ROOT_URLCONF = '%s.settings.urls' % PROJECT_MODULE

TEMPLATE_DIRS = (
    root('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'south',
    'interface',
    'django_extensions',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(levelname)s %(asctime)s |'
                       ' %(pathname)s:%(lineno)d (in %(funcName)s) |'
                       ' %(message)s ')
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': root('%s.log' % PROJECT_MODULE),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        PROJECT_MODULE: {
            'handlers': ['logfile'],
            'level': 'DEBUG'
        }
    }
}
