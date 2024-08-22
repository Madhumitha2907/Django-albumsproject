from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('create/', views.song_create, name='song_create'),
    path('<int:pk>/edit/', views.song_update, name='song_update'),
    path('<int:pk>/delete/', views.song_delete, name='song_delete'),
   # path('<int:song_id>/', views.song_detail, name='song_detail'),
    path('<int:song_id>/', views.song_detail, name='song_detail'),
]