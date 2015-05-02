from django.conf.urls import patterns, url
from obay import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'add_item/$', views.add_item, name='add_item'),
    url(r'^item/(?P<item_name_slug>[\w\-]+)/$', views.itemview, name='item'),
)