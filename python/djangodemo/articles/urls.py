from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^/?$', 'articles.views.home', name='home'),
    url(r'^article/([a-zA-Z0-9_-]*)$', 'articles.views.article'),
)
