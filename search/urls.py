from django.urls import path
from search import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.show, name='show'),
    path('register/', views.register, name='register'),
    path('login/', views.myLogin, name='login'),
    path('liked/', views.liked, name='liked'),
    path('playlist/', views.playlist, name='playlist'),
    path('search/', views.search, name='search'),
    path('search-playlist/', views.search, name='search-playlist'),
    path('logout/', views.myLogin, name='logout'),
    path('liked-playlist/', views.liked, name='liked-playlist'),

]

# Necessary for images to be loaded correctly
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)