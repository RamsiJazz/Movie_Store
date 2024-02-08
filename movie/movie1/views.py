from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def killer(request):
    return render(request, 'killer.html')


def haunt(request):
    return render(request, 'haunt.html')


def world(request):
    return render(request, 'world.html')


def reptile(request):
    return render(request, 'reptile.html')


def tetris(request):
    return render(request, 'tetris.html')


def plane(request):
    return render(request, 'plane.html')
