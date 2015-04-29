from django.conf.urls import patterns, url
from obay import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'add_item/$', views.add_item, name='add_item'),
    url(r'^item/(?P<item_name_slug>[\w\-]+)/$', views.itemview, name='item'),
    url(r'^item/(?P<item_name_slug>[\w\-]+)/add_bid/$', views.add_bid, name='add_bid'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
)