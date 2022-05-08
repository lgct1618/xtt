from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    new_videos = {
        1:"teste1",
        2:"teste2",
        3:"teste3",
        4:'teste4',
        5:'teste',
        6:'teste222'
    }

    name_videos = {"nov" : new_videos}


    return render(request, 'index.html', name_videos)

def upload(request):
    return render(request, 'upload.html')

def video(request):
    return render(request, 'video.html')
