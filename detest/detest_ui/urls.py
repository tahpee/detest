from django.conf.urls import patterns, url
from detest_ui import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^index.html$', views.index, name='index'),
                       url(r'^projects$', views.project_list, name='project_list'),
                       url(r'^buttons/$', views.buttons, name='buttons'),
                       url(r'^project/(?P<pk>\d+)/$', views.ProjectView.as_view(), name='project'),
                       # url(r'^login/$', views.login_view),
                       # url(r'^logout/$', views.logout_user),
                       )
