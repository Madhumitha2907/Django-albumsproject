from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_singer_list, name='song_singer_list'),
    path('create/', views.song_singer_create, name='song_singer_create'),
    path('<int:pk>/edit/', views.song_singer_update, name='song_singer_update'),
    path('<int:pk>/delete/', views.song_singer_delete, name='song_singer_delete'),
]
