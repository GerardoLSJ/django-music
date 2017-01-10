# pylint: disable=C0111
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Album

def index(request):
    """ return all elements"""
    all_albums = Album.objects.all()
    html = ''
   #template = loader.get_template('music/index.html')
    context = {
        'all_albums' : all_albums,

    }
    return render(request, 'music/index.html',context)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + " </h2>")

