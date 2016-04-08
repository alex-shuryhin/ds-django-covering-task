from book_store.views import *
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', IndexView.as_view(), name='index'),
        url(r'^register/$', register, name='register'),
        url(r'^login/$', user_login, name='login'),
        url(r'^logout/$', user_logout, name='logout'),
        url(r'^user/$', user_test, name='user_test'),
        url(r'^add_book/$', book_add, name='book_create'),
        url(r'^edit_book/(?P<book_id>\d+)/$', book_edit, name='book_edit'),
        url(r'^requests/$',RequestsView.as_view(), name='requests'),
)