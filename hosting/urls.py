from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_content, name='main'),
    url(r'^activity/detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^hosting/$', views.host, name='hosting'),
    url(r'^hosting/0/$', views.host0, name='host0'),
    url(r'^hosting/1/$', views.host1, name='host1'),
    url(r'^hosting/2/$', views.host2, name='host2'),
	url(r'^hosting/4/(?P<pk>\d+)/$', views.host4, name='host4'),
	url(r'^hosting/8/(?P<pk>\d+)/$', views.host8, name='host8'),
]
