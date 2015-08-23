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

                       url(r'^admin/projects$', admin_views.project_list, name='project_list'),
                       url(r'^admin/new_project$', admin_views.new_project, name='new_project'),
                       url(r'^admin/delete_project$', admin_views.delete_project, name='delete_project'),
                       url(r'^admin/project_details/(?P<project>\d+)/$', admin_views.project_view, name='project'),

                       )
