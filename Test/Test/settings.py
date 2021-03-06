"""
Django settings for Test project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
'''
SECRET_KEY是Django根据自己算法生成的一大串随机数，
本质是个加密盐，用于防止CSRF（Cross-site request forgery）跨站请求伪造攻击
部署到生产环境时
# 方法一: 从环境变量中读取SECRET_KEY
import os
SECRET_KEY = os.environ['SECRET_KEY']
# 方法二: 从服务器上Django项目文件价外的某个文件读取
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
'''
SECRET_KEY = 'ms^cw#z%zp0(a$6idq+b((mv$!)q5zyu2xtyxd!*uv+w(vkh)s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
'''
默认值为空[]。设置ALLOWED_HOSTS是为了限定用户请求中的host值，以防止黑客构造包来进行头部攻击。该选项正确设置方式如下:
    DEBUG=True:  ALLOWED_HOSTS可以为空，也可设置为['127.0.0.01', 'localhost']
    DEBUG=False: ALLOWED_HOSTS=['46.124.78.xx', 'www.bat.com'，'127.0.0.1']
当你关闭DEBUG时，HOST一般为服务器公网IP或者注册域名。 当你还需要使用子域名时，你可以用'.bat.com'。
它将匹配bat.com, www.bat.com和news.bat.com。在正式部署项目时，请尽量不要设置ALLOWED_HOSTS=['*']。
'''

#SITE_ID = 1

# Application definition
# 只有对列入此项的APP, Django才会生成相应的数据表。
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'file_upload',
    'pic_upload',
    'request_demo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'Test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Test', # 数据库名称，数据库需要自己提前建好
        'USER':'root',
        'PASSWORD':'weipeng1.2.3.4.',
        'HOST':'127.0.0.1',
        'PORT':'3306',          # 数据库使用的端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

 
LANGUAGE_CODE = 'zh-Hans' 

TIME_ZONE = 'Asia/Shanghai' # 设置时区

USE_I18N = True  # 默认为True，是否启用自动翻译系统

USE_L10N = True  # 默认False，以本地化格式显示数字和时间

USE_TZ = True # 默认值True。若使用了本地时间，必须设为False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
'''
一般设置如下。STATIC_URL是静态文件URL，
设置后可以通过使用{% static 'img/xxx.jpg' %}方式直接访问/static/文件夹里的静态文件。
如果你设置了STATIC_ROOT, 当你运行"python manage.py collectstatic"命令的时候，
Django会将各app下所有名为static的文件夹及其子目录复制收集到STATIC_ROOT。
把静态文件集中一起的目的是为了更方便地通过Apache或Nginx部署。
'''
STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 如果你还有一些文件夹中也有静态文件，
# 可是文件夹并不是以static命名也不在static子目录里，此时你也希望搜集使用那些静态文件，
STATICFILES_DIRS = [os.path.join(BASE_DIR,"static"),]

# media文件夹一般用于放置用户上传的文件。
# 对于此文件夹的权限设置异常重要，因为用户可能会上传可执行的文件，影响网站和服务器的安全，
# specify media root for user uploaded files,
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# 基本设定
# ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_EMAIL_REQUIRED = True
# LOGIN_REDIRECT_URL = '/myaccounts/profile/' # 登录或注册后自动跳转到/accounts/profile/

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )
# 邮箱设定
# EMAIL_HOST = 'smtp.qq.com'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = '1453313323@qq.com' # 你的 QQ 账号和授权码
# EMAIL_HOST_PASSWORD = 'tskfhkyieisshcbd'
# EMAIL_USE_TLS = True  # 这里必须是 True，否则发送不成功
# EMAIL_FROM = '1453313323@qq.com' # 你的 QQ 账号
# DEFAULT_FROM_EMAIL = '1453313323@qq.com'

