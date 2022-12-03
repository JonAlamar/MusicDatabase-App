from django.db import models


class Music(models.Model):
    music_title = models.CharField(max_length=100)
    music_artist = models.CharField(max_length=100)
    music_albumpic = models.CharField(max_length=100)


class Playlist(models.Model):
    music_title = models.CharField(max_length=100)
    music_artist = models.CharField(max_length=100)
    music_albumpic = models.CharField(max_length=100)

    ##do not need to create a user table, django already has it when database was created, it's called auth_user.
    ## in the view just do if form.is.valid(): form.save()   return
    ## then redirect user to some page after, what is difference between redirect and return?

    ##make a spinning loading logo for 2 seconds after completeiting search, use javascript to animate loop pics
    ##how do you make it so it will do spin animate only if user searches with post, and not a normal url render?

    ##for the search bar at top is it submit type?

    ##after logging in, this is the way you remember the logged in person each time they browse through pages
    ##one way to do this is to leave a cookie, django will do for us, the login(request, user) method does this

    ##once user is logged in, want to make the show page shows heart buttons, if the aren't logged in they dont
    ##see any heart images.
    ##in template {% if user.is_authenticated %}
    ##                 stuff
    ##             {% endif %}
    ## one application should be accounts, then another app named after application

    ##in ajax, is the return display actualy being loaded each time or is only the element changing


