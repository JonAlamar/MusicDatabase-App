from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Music, Playlist
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages



# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def show(request):
    music = Music.objects.all()
    playlist_ids = []
    if request.user.is_authenticated:
        playlist = Playlist.objects.filter(user=request.user)
        for list in playlist:
            playlist_ids.append(list.music_id)

    print("The playlist", playlist_ids)
    if request.method == 'POST':
        searched = request.POST.get('searched')

        context = {'music': music,
                   'searched': searched, 'playlist_ids': playlist_ids}
        return render(request, 'homepage.html', context)

    else:
        context = {'music': music, 'playlist_ids': playlist_ids}
        return render(request, 'homepage.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def myLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('show')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"form": form})


def liked(request):
    if request.method == 'POST':
        music_id = request.POST['music-id']
        like_status = request.POST['like-status']
        like_status = int(like_status)
        print(music_id)
        if like_status == 1:
            if Playlist.objects.filter(user=request.user, music_id=music_id).count() == 0:
                Playlist.objects.create(user=request.user, music_id=music_id)
            else:
                messages.error(request, "It is already in your playlist!")
            return redirect('show')
        elif like_status == 0:
            item = Playlist.objects.get(music_id=music_id, user=request.user)
            item.delete()
            return redirect('show')
    else:
        return redirect('show')


def playlist(request):
    playlist = Playlist.objects.filter(user=request.user)
    current_user = get_user_model()
    playlist_ids = []
    for list in playlist:
        playlist_ids.append(list.music_id)

    return render(request, 'playlist.html', {'playlist_ids': playlist_ids, 'playlist': playlist, 'current_user': current_user})
