from django.conf.urls import patterns, include, url
from painting.views import paints


urlpatterns = patterns('',
    ('^$', paints),
)
