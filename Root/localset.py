'''local Settings
'''
import os
from pathlib import Path

CSRF_TRUSTED_ORIGINS = ['https://github.com/','https://irabs174-symmetrical-umbrella-jj5qg4p7xpwh54gv-8000.preview.app.github.dev']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wz-w_w(th@)207i9=5&0*3*ga^0w&e)6&)45ou$r@5)7&jqmi$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Internationalization

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Static files (CSS, JavaScript, Images)
#STATIC_URL = os.path.join(BASE_DIR, 'static/')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# User Authentications REDIRECT:
LOGIN_REDIRECT_URL='/accounts/panel'
LOGOUT_REDIRECT_URL = '/'