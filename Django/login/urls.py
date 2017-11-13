#coding:utf-8

from django.conf.urls import url, include, patterns

urlpatterns = patterns('Django.login.views',
					   (r'^index/$', 'index'),
					   (r'^login/$', 'login')
					   )