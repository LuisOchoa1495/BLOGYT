from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['eighta.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'eighta$blogdb',
        'USER': 'eighta',
        'PASSWORD': 'Luisochoa1495*',
        'HOST': 'eighta.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

#CKEDITOR SETTINGS
CKEDITOR_UPLOAD_PATH='upload/'
CKEDITOR_IMAGE_BACKEND='pillow'
CKEDITOR_JQUERY_URL='https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_CONFIGS={
    'default':{
        'toolbar':'Custom',
        'toolbar_custom':[
            ['Bold', 'Italic', 'Underline',],
            ['NumberedList', 'BulletedList','-', 'Outdent','Inde','-','Justified'],
            ['TextColor','Format','FontSize','Link'],
            ['Smiley', 'Image','Iframe'],
            ['RemoveFormat', 'Source'],
        ],
        'stylesSet':[
        ],
    }
}
# EMAIL SETTINGS
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = get_secret('EMAIL')
# EMAIL_HOST_PASSWORD = get_secret('PASS_EMAIL')
# EMAIL_PORT = 587