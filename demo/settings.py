# Django settings for demo project.
import os
import sys
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

sys.path.insert(0, PROJECT_DIR)

gettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'demo.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, "static")
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "site-static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'kr&amp;m^8_$@=%_%v*o@!$t2qye_bz3ohkrh_ug3^rhq)w99apuaj'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware', #CMS
    'cms.middleware.page.CurrentPageMiddleware', #CMS
    'cms.middleware.user.CurrentUserMiddleware', #CMS
    'cms.middleware.toolbar.ToolbarMiddleware', #CMS
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media', #CMS
    'sekizai.context_processors.sekizai', #CMS
)

ROOT_URLCONF = 'demo.urls'

WSGI_APPLICATION = 'demo.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # CMS related apps
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'reversion',
    'cms.plugins.text',
    'polls',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cms.plugins.link',
    'plugins.bootstrap_button',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# django CMS settings
LANGUAGES = [
    ('en', gettext('English')),
    ('es', gettext('Spanish')),
]

CMS_LANGUAGES = LANGUAGES
CMS_HIDE_UNTRANSLATED = True
CMS_LANGUAGE_CONF = {
        'es': ['en',],
    }


CMS_TEMPLATES = (
    ('home.html', gettext("Homepage")),
    ('subpage.html', gettext("Secondary Page")),
)

CMS_PLACEHOLDER_CONF = {
    'home-hero': {
        'name': gettext('Hero'),
        'plugins': ['TextPlugin', 'BootstrapButtonPlugin',],
    },
    'home-col-1': {
        'name': gettext('Column 1'),
        'plugins': ['TextPlugin', 'BootstrapButtonPlugin',],
    },
    'home-col-2': {
        'name': gettext('Column 2'),
        'plugins': ['TextPlugin', 'BootstrapButtonPlugin',],
    },
    'home-col-3': {
        'name': gettext('Column 3'),
        'plugins': ['TextPlugin', 'PollPlugin', ],
        'limits': {
            'global': 2,
            'TextPlugin': 1,
            'PollPlugin': 1,
        },
    },
    'subpage_content': {
        'name': gettext('Content'),
    },
}

CMS_URL_OVERWRITE = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_REDIRECTS = True
CMS_SOFTROOT = True
CMS_PERMISSION = True
CMS_SHOW_START_DATE = True
CMS_SHOW_END_DATE = True 
CMS_SEO_FIELDS = True 

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
