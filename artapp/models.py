from django.db import models


# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=20, verbose_name='类别', unique=True)
    author = models.CharField(max_length=10, blank=True)


# 小说模型
class Art(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='小说名')
    author = models.CharField(max_length=10, blank=True, verbose_name='作者')
    summary = models.TextField(verbose_name='简介')
    # image_url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', verbose_name='小说图片')
    counter = models.IntegerField(default=0, verbose_name='浏览次数')
    publish_time = models.DateTimeField(auto_now_add=True)
    tags = models.ForeignKey(book, on_delete=models.SET_NULL, null=True)



