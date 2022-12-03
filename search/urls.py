from django.urls import path
from search import views

urlpatterns = [
    path('', views.homepage),
    path('show/', views.show, name='show')
]
