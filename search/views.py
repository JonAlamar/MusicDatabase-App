from django.shortcuts import render
from .models import Music

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def show(request):
    music = Music.objects.all()

    if request.method == 'POST':
        searched = request.POST.get('searched')

        context = {'music': music,
                   'searched': searched}
        return render(request, 'homepage.html', context)

    else:
        context = {'music': music}
        return render(request, 'homepage.html', context)
