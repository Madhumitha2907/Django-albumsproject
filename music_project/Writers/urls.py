# writers/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.writer_list, name='writer_list'),
    path('create/', views.writer_create, name='writer_create'),
    path('<int:pk>/', views.writer_detail, name='writer_detail'),
    path('<int:pk>/edit/', views.writer_update, name='writer_update'),
    path('<int:pk>/delete/', views.writer_delete, name='writer_delete'),
]
