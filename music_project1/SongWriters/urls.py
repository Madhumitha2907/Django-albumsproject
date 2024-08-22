from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_writer_list, name='song_writer_list'),
    path('create/', views.song_writer_create, name='song_writer_create'),
    path('<int:pk>/edit/', views.song_writer_update, name='song_writer_update'),
    path('<int:pk>/delete/', views.song_writer_delete, name='song_writer_delete'),
]
