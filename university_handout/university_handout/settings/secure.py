from decouple import config


SECRET_KEY = config('SECRET_KEY')
PREPEND_WWW = config('PREPEND_WWW', cast=bool)

# ######################### #
#         DATABASE          #
# ######################### #

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'universitydb',
        'USER': 'university',
        'PASSWORD': '1928374655db',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# ############################ #
#      SSL CONFIGURATION       #
# ############################ #
SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', cast=bool)
SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', cast=bool)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', cast=bool)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', cast=bool)
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', cast=int)

if config('SECURE_PROXY_SSL_HEADER', cast=bool):
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_REDIRECT_EXEMPT = []
SECURE_REFERRER_POLICY = config('SECURE_REFERRER_POLICY')
SECURE_SSL_HOST = config('SECURE_SSL_HOST')
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', cast=bool)

# ############################ #
#           Security           #
# ############################ #
CSRF_COOKIE_AGE = config('CSRF_COOKIE_AGE', cast=int)
CSRF_COOKIE_HTTPONLY = config('CSRF_COOKIE_HTTPONLY', cast=bool)
CSRF_COOKIE_NAME = config('CSRF_COOKIE_NAME')
CSRF_COOKIE_PATH = config('CSRF_COOKIE_PATH')
CSRF_COOKIE_SAMESITE = config('CSRF_COOKIE_SAMESITE').capitalize()
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', cast=bool)
CSRF_USE_SESSIONS = config('CSRF_USE_SESSIONS', cast=bool)
CSRF_HEADER_NAME = config('CSRF_HEADER_NAME')
