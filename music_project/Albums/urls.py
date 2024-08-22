from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('create/', views.album_create, name='album_create'),
    path('<int:pk>/edit/', views.album_update, name='album_update'),
    path('<int:pk>/delete/', views.album_delete, name='album_delete'),
    path('<int:album_id>/', views.album_detail, name='album_detail'),
    #path('<int:album_id>/', album_detail, name='album_detail'),
    path('<int:song_id>/', views.song_detail, name='song_detail'),
]
