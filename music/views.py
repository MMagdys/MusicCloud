from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album

# Create your views here.

class IndexView(generic.ListView):

    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()



class DetailView(generic.DetailView):

    model = Album
    template_name = 'music/detail.html'



class AlbumAdd(CreateView):

    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']



class AlbumUpdate(UpdateView):

    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']



class AlbumDelete(DeleteView):

    model = Album
    success_url = reverse_lazy('music:index')