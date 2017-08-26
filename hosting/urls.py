from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_content, name='main'),
    url(r'^activity/detail/(?P<pk>\d+)/$', views.detail, name='detail'),
]
