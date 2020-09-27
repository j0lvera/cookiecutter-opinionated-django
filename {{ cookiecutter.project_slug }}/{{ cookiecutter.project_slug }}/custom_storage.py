from storages.backends.s3boto3 import S3Boto3Storage
from {{ cookiecutter.project_slug }}.settings import env


class MediaStorage(S3Boto3Storage):
    bucket_name = env("AWS_STORAGE_BUCKET_NAME")
    location = "media"
