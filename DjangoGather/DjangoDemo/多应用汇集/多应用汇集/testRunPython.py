import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#&!*ia1^l6%^_$8-*wyjk&_8=_c^_*dnbp6(8$!r@9_lp^d^n^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # '福解析.system',
    # '福解析.demo',
    # '福解析.generator', 
] + [
    f'福解析.{app_name}'
    for app_name in os.listdir(BASE_DIR / '福解析')
    if os.path.isdir(BASE_DIR / '福解析' / app_name) and os.path.exists(BASE_DIR / '福解析' / app_name / '__init__.py')
]


#  + [
#     f'福解析.{app_name}.apps.{app_name}Config'
#     for app_name in os.listdir(BASE_DIR / '福解析')
#     if os.path.isdir(BASE_DIR / '福解析' / app_name) and os.path.exists(BASE_DIR / '福解析' / app_name / '__init__.py')
# ]


print(INSTALLED_APPS)


