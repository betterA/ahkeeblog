from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post')
]