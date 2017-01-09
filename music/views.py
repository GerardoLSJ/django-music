from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Music app Homepage</h1>')