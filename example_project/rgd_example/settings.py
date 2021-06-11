import os
from typing import List

try:
    import re

    import osgeo

    libsdir = os.path.join(os.path.dirname(os.path.dirname(osgeo._gdal.__file__)), 'GDAL.libs')
    libs = {re.split(r'-|\.', name)[0]: os.path.join(libsdir, name) for name in os.listdir(libsdir)}
    GDAL_LIBRARY_PATH = libs['libgdal']
    GEOS_LIBRARY_PATH = libs['libgeos_c']
except Exception:
    # TODO: Log that we aren't using the expected GDAL wheel?
    pass

SECRET_KEY = 'example-secret'

DEBUG = True

ALLOWED_HOSTS: List[str] = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'oauth2_provider',
    # 'oauth2_provider.models.Application',
    's3_file_field',
    # RGD Apps
    'django.contrib.gis',
    'rgd',
    'rgd_3d',
    'rgd_fmv',
    'rgd_geometry',
    'rgd_imagery',
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

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'django',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }
]

SITE_ID = 1

STATIC_URL = '/static/'

ROOT_URLCONF = 'rgd_example.urls'
WSGI_APPLICATION = 'rgd_example.wsgi.application'

if False:  # 'AWS_ACCESS_KEY_ID' in os.environ:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_S3_REGION_NAME = os.environ.get('AWS_DEFAULT_REGION', 'us-east1')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_SIGNATURE_VERSION = 's3v4'
else:
    DEFAULT_FILE_STORAGE = 'minio_storage.storage.MinioMediaStorage'
    MINIO_STORAGE_ENDPOINT = 'minio:9000'
    MINIO_STORAGE_USE_HTTPS = False
    MINIO_STORAGE_ACCESS_KEY = 'minioAccessKey'
    MINIO_STORAGE_SECRET_KEY = 'minioSecretKey'
    MINIO_STORAGE_MEDIA_BUCKET_NAME = 'rgd-example'
    MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
    MINIO_STORAGE_AUTO_CREATE_MEDIA_POLICY = 'READ_WRITE'
    MINIO_STORAGE_MEDIA_USE_PRESIGNED = True
