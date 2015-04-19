from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'detest.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'', include('detest_ui.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout'),
                       url(r'^', include('django.contrib.auth.urls')),
                       )
