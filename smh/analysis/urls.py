from django.conf.urls import url

from . import views

app_name = 'smh2'
urlpatterns = [
    url(r'^tweet/$', views.tweet, name='tweet'),
    url(r'^results/$', views.results, name='results'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]
