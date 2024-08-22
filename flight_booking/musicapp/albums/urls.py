
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     path('profile/', views.profile_view, name='profile'),
    path('', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('api/albums/', views.album_list, name='album_list'),
     path('api/albums/', views.AlbumListView.as_view(), name='album_list'),
    path('album_list/', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/add/', views.album_add, name='album_add'),
    path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),
    
    
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
     path('singer/<str:name>/', views.singer_detail, name='singer_detail'),
     path('writer/<int:pk>/', views.writer_detail, name='writer_detail'),
     
   path('singers/songs_by_singer/<str:singer_name>/',views.get_songs_by_singer,name='get_songs_by_singer'),
    path('writers/songs_by_writer/<str:writer_name>/',views.get_songs_by_writer,name='get_songs_by_writer'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

