from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta(object):
        db_table = 'custom_user'

    password = models.CharField(blank=False, null=False, max_length=150)
