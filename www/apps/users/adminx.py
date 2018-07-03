"""
__author__  : 'demon'
__date__  : '2018/7/3/003 10:20'
"""
import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '西门庆小说'
    site_footer = '一个盗版网站'
    menu_style = 'accordion'

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)