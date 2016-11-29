from django.conf.urls import url

from . import views

app_name = 'smh2'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_user, name='login'),
]
