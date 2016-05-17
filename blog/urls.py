from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^crear/', views.crear),
    #url(r'^post/new/$', views.post_new, name='post_new'),
]