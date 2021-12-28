from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TimeStampedModel
from django.db import models


# Create your models here.
class CustomUser(TimeStampedModel, AbstractUser):
    pass

    def __str__(self):
        return self.username
