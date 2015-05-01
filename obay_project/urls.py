from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from registration.backends.simple.views import RegistrationView

# Redirect user to the index instead of showing a registration complete page
# class MyRegistrationView(RegistrationView):
#     def get_success_url(self,request, user):
#         return '/obay/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'obay_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'obay.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^obay/', include('obay.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
            'serve',
            {'document_root': settings.MEDIA_ROOT}), )


