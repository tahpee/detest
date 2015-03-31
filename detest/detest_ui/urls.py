from django.conf.urls import patterns, url
from detest_ui import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^buttons/$', views.buttons, name='buttons'),
                       url(r'^login/$', views.login_view),
                       # url(r'^logout/$', views.logout_user),
                       )
