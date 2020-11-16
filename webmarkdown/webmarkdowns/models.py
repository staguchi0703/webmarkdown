import datetime
from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from django.utils import timezone

# Create your models here.

class Projects(models.Model):
    """プロジェクトモデル"""

    project_name = models.CharField(max_length=255, null=True, blank=True, default='unknown')


    def __str__(self):
        return self.project_name.__str__()


class Articles(models.Model):
    """記事モデル"""

    project = models.ForeignKey(Projects, verbose_name='種類', on_delete=models.PROTECT, null=True, blank=True)
    owner = models.ForeignKey( CustomUser, verbose_name='使用者', on_delete=models.PROTECT, null=True, blank=True)
    time_stamp = models.DateTimeField(default=timezone.now, null=True, blank=True)
    markdown_txt = models.TextField(verbose_name='markdown text', null=True, blank=True, default='# Title')

