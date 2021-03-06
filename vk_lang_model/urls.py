from django.conf.urls import patterns, include, url

from django.contrib import admin
from ui import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vk_lang_model.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^person/([0-9]+)/$', views.render_person),
)
