from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'detest.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'', include('detest_ui.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^login/$', login),
                       # url(r'^logout/$', logout),
                       # url(r'^', include('django.contrib.auth.urls')),
                       )
