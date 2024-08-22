# singers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.singer_list, name='singer_list'),
    path('create/', views.singer_create, name='singer_create'),
    path('<int:pk>/', views.singer_detail, name='singer_detail'),
    path('<int:pk>/edit/', views.singer_update, name='singer_update'),
    path('<int:pk>/delete/', views.singer_delete, name='singer_delete'),
]
