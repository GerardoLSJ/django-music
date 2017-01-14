# pylint: disable=C0111
# pylint: disable=E1101
#from django.http import HttpResponse
#from django.template import loader
#from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    """ return all elements"""
    all_albums = Album.objects.all()
   #template = loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums,

    }
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    """
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404('Album does not exist')
    """
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/detail.html', {'album':album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',{
            'album':album,
            'error_message': 'yo, not that song'
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album':album})