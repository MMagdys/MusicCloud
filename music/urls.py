from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/12/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/add
    url(r'album/add/$', views.AlbumAdd.as_view(), name='add-album'),

    # /music/album/<pk>
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='update-album'),

    # /music/album/<pk>/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='delete-album')

]
