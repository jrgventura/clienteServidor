from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^crear/', views.crear),
    url(r'^mes/', views.fecha_list),
    url(r'^planilla/(\d+)/$', views.planilla),
    #url(r'^planilla/()', views.planilla),

    #url(r'^post/new/$', views.post_new, name='post_new'),

]
