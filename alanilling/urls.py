from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.conf import settings

urlpatterns = patterns('',
    url(
        r'^$', view=TemplateView.as_view(template_name='homepage.html'), name='homepage'
    ),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
)
