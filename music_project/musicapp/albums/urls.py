# albums/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/add/', views.album_add, name='album_add'),
    path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),
    #path('song/<int:pk>/', views.song_detail, name='song_detail'),
    #path('song/add/', views.song_add, name='song_add'),  
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('song/add/', views.song_add, name='song_add'),
    path('song/edit/<int:pk>/', views.song_edit, name='song_edit'),
    path('song/delete/<int:pk>/', views.song_delete, name='song_delete'),
    path('singers/', views.singer_list, name='singer_list'),

    path('singer/<int:pk>/', views.singer_detail, name='singer_detail'),
    path('singer/add/', views.singer_add, name='singer_add'),
    path('singer/edit/<int:pk>/', views.singer_edit, name='singer_edit'),
    path('singer/delete/<int:pk>/', views.singer_delete, name='singer_delete'),
     path('writers/', views.writer_list, name='writer_list'),
    path('writer/<int:pk>/', views.writer_detail, name='writer_detail'),
    path('writer/add/', views.writer_add, name='writer_add'),
    path('writer/edit/<int:pk>/', views.writer_edit, name='writer_edit'),
    path('writer/delete/<int:pk>/', views.writer_delete, name='writer_delete'),
    path('song/<int:song_id>/add_singer/', views.add_singer_to_song, name='singer_add'),
    path('song/<int:song_id>/add_writer/', views.add_writer_to_song, name='writer_add'),
]
