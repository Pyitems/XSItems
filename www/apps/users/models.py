from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserInfo(AbstractUser):
    """
    用户信息
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')
    birthday = models.DateTimeField(null=True, blank=True, verbose_name='出生年月')
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')),
                              default='female', verbose_name='性别')
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name='手机号')
    email = models.EmailField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username