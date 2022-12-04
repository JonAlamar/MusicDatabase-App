from django.shortcuts import render, redirect
from .models import Music
from django.contrib.auth.forms import UserCreationForm

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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})