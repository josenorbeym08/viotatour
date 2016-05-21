import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#encoding:utf-8


SECRET_KEY = 'v!q#6g(en1_!f1=bfh0c%qy(!krrou%0y!m)ee8s27#nwecdar'


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'django_extensions',
    'vioturismo.apps.sitios',
    'vioturismo.apps.sturist',
    'vioturismo.apps.webServices.wsSitiostcs',
#    'django.contrib.admindocs',
#    'vioturismo.apps.bitacora',
    'vioturismo.apps.gmaps',


)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'audit_log.middleware.JWTAuthMiddleware',
    'audit_log.middleware.UserLoggingMiddleware',
    
)

ROOT_URLCONF = 'vioturismo.urls'

AUTH_PROFILE_MODULE = 'sitios.userProfile'

WSGI_APPLICATION = 'vioturismo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#MANAGERS = ADMINS
#MOTOR_DB == 'sqlite'


#base de datos modi
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}






#if MOTOR_DB == 'mysql':
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'vio',
#        'USER': 'root',                      # Nol at used with sqlite3.
#        'PASSWORD': 'root',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',  
#    }
#}

#if MOTOR_DB == 'sqlite':
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(__file__),'vio.db'),
        'USER': 'root',                      # Nol at used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  
    }
}




TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "vioturismo.apps.context_processors.my_processor",
)


#MIDDLEWARE_CLASSES = (
#    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
#)







LANGUAGE_CODE = 'es-co'
#'UTC'
#America/Bogota
TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = False


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__),'media/'))




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR + '/static/',
    #os.path.join(BASE_DIR+'/static/'),

)

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
    #os.path.join(BASE_DIR+'/templates/'),

)


#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()


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


LOGIN_REDIRECT_URL = '/'

#django_smtp_ssl.SSLEmailBackend
# CONFIGURACION DEL SERVIDOR DE CORREO
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'vioturismopro@gmail.com'
EMAIL_HOST_PASSWORD = 'Jn123456'
EMAIL_USE_TLS = True


URL_LOGIN = '/login/'


#Para cuando corra collestatic
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS = (
#    BASE_DIR + '/static',
#)

#TEMPLATE_DIRS = (
#    BASE_DIR + '/templates/',
#)

#Parse database configuration from $DATABASE_URL
#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
#ALLOWED_HOSTS = ['*']

# Static asset configuration
#STATIC_ROOT = 'staticfiles'
#STATIC_URL = '/static/'