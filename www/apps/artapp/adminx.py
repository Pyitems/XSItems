"""
__author__  : 'demon'
__date__  : '2018/7/3/003 18:37'
"""
import xadmin

from .models import ArtTag, Art
# 小说或文章标签类型的模型
class ArtTagAdmin(object):
    list_display = ['title', 'add_time', 'modify_time']

xadmin.site.register(ArtTag, ArtTagAdmin)

# 小说文章的模型
class ArtAdmin(object):
    list_display = ['title', 'author', 'img', 'counter', 'publish_time']

xadmin.site.register(Art, ArtAdmin)