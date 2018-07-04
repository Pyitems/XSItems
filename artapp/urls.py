"""XSProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from artapp import views, views_art

urlpatterns = [
    url(r'^tags/', views.add_tags),
    url(r'^tags_list/(\d+)/$', views.tag_list, name='tags_list'),
    url(r'^index/', views.index),
    url(r'^del_tag/', views.delete_tag),
    url(r'art_edit', views_art.art_edit, name='art_edit'),
    url(r'search/', views_art.search)
]
