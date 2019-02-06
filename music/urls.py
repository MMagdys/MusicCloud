from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/12/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]
