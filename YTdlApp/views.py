from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def index(request):
    if request.method == 'POST':
        link = request.POST['link']
        video = YouTube(link)
        stream = video.streams.first()
        stream.download('~/Downloads')
        return render(request,'index.html',{'msg':'Video downloaded'})
    return render(request,'index.html',{'msg':'Video not downloaded'})
