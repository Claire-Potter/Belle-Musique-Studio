"""
Belle Musique Studio custom storages configuration
"""
from django.conf import settings
# The Django settings file contains all of the configuration for
# # a web application.
from storages.backends.s3boto3 import S3Boto3Storage
# Amazon Simple Storage Service (S3)


class StaticStorage(S3Boto3Storage):
    """
    Set static files location as Amazon S3
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Set media files location as Amazon S3
    """
    location = settings.MEDIAFILES_LOCATION
