from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^secure-admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^secure-admin/', include(admin.site.urls)),
    url(r'^book_store/', include('book_store.urls', namespace="book_store")),


)
