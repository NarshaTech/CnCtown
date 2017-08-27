from django.conf.urls import url

urlpatterns = [
  url(r'^login/$', views.signin, name='login'),
]
