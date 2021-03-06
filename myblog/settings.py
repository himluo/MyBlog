"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tk@==0#uuu5g0$&r8^v=w@6%mlrw8b@4qtn%42-26z1n1^arxr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["www.himluo.com", "127.0.0.1", 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'blogs.apps.BlogsConfig',
    'webpack_loader',
    'ckeditor',
    'ckeditor_uploader',
    'hitcount',
    'users',
]

AUTH_PROFILE_MODULE = 'users.MyUser'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'blogs'),
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'PAGE_SIZE': 5,
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/'
    }
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'root',
        'PASSWORD': '123698745',
        'HOST': '',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = "upload/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_ArticleConfig': [
            {'name': 'clipboard', 'items': ['Undo', 'Redo']},
            {'name': 'styles', 'items': ['Styles', 'Format']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Strike', '-', 'RemoveFormat']},
            {'name': 'paragraph', 'items': [
                'NumberedList',
                'BulletedList',
                '-',
                'Outdent',
                'Indent',
                '-',
                'Blockquote'
            ]},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'insert', 'items': ['Image', 'EmbedSemantic', 'Table', 'CodeSnippet']},
            {'name': 'tools', 'items': ['Maximize']},
            {'name': 'editing', 'items': ['Scayt']},
        ],

        'toolbar': 'ArticleConfig',  # put selected toolbar config here
        'tabSpaces': 4,
        'extraPlugins': 'autoembed,embedsemantic,image2,uploadimage,uploadfile,codesnippet',
        'removePlugins': 'image',
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'filebrowserBrowseUrl': '/ckeditor/browse/',
        'height': 461,
        'contentsCss': ['https://cdn.ckeditor.com/4.6.0-441b33b/standard-all/ckeditor/contents.css'],
        'bodyClass': 'article-editor',
        'format_tags': 'p;h1;h2;h3;pre',
        'removeDialogTabs': 'image:advanced;link:advanced',

        'stylesSet': [
            {'name': 'Marker',	'element': 'span', 'attributes': {'class': 'marker'}},
            {'name': 'Cited Work',	'element': 'cite'},
            {'name': 'Inline Quotation', 'element': 'q'},
            {
                'name': 'Special Container',
                'element': 'div',
                'styles': {
                    'padding': '5px 10px',
                    'background': '#eee',
                    'border': '1px solid #ccc'
                }
            },
            {
                'name': 'Compact table',
                'element': 'table',
                'attributes': {
                    'cellpadding': '5',
                    'cellspacing': '0',
                    'border': '1',
                    'bordercolor': '#ccc'
                },
                'styles': {
                    'border-collapse': 'collapse'
                }
            },
            {'name': 'Borderless Table', 'element': 'table', 'styles': {
                'border-style': 'hidden',
                'background-color': '#E6E6FA'
            }},
            {'name': 'Square Bulleted List', 'element': 'ul', 'styles': {'list-style-type': 'square'}},
            {'name': 'Illustration', 'type': 'widget', 'widget': 'image', 'attributes': {
                'class': 'image-illustration'
            }},
            {'name': '240p', 'type': 'widget', 'widget': 'embedSemantic', 'attributes': {'class': 'embed-240p'}},
            {'name': '360p', 'type': 'widget', 'widget': 'embedSemantic', 'attributes': {'class': 'embed-360p'}},
            {'name': '480p', 'type': 'widget', 'widget': 'embedSemantic', 'attributes': {'class': 'embed-480p'}},
            {'name': '720p', 'type': 'widget', 'widget': 'embedSemantic', 'attributes': {'class': 'embed-720p'}},
            {'name': '1080p', 'type': 'widget', 'widget': 'embedSemantic', 'attributes': {'class': 'embed-1080p'}}
        ],
        'language': 'zh-cn',
    }
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

