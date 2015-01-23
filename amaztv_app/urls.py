from django.conf.urls import patterns, url

from amaztv_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^tag/(?P<tag>\S+)/$', views.tag, name='tag'),
    url(r'^(?P<cat>\S+)/$', views.category, name='category'),
)