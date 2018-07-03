from django.db import models


# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=20, verbose_name='类别', unique=True),
    author = models.CharField(max_length=10, blank=True),
