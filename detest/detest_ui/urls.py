from django.conf.urls import patterns, url
from detest_ui import views
from detest_ui import admin_views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^index.html$', views.index, name='index'),
                       url(r'^dashboard/(?P<project>[\w\s]+)/$', views.project, name='project'),
                       url(r'^design/(?P<project>[\w\s]+)/$', views.design_top, name='project'),
                       url(r'^projects$', views.project_list, name='project_list'),
                       url(r'^buttons/$', views.buttons, name='buttons'),
                       url(r'^project_details/(?P<pk>\d+)/$', views.ProjectView.as_view(), name='project'),
                       url(r'^admin/projects$', admin_views.project_list, name='project_list'),
                       # url(r'^login/$', views.login_view),
                       # url(r'^logout/$', views.logout_user),
                       )
