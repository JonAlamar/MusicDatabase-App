from django.urls import path
from search import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage),
    path('show/', views.show, name='show'),
    path('register/', views.register, name='register'),
    path('login/', views.myLogin, name='login'),
    path('liked/', views.liked, name='liked'),
    path('show/playlist/', views.playlist, name='playlist'),
]


# Necessary for images to be loaded correctly
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)