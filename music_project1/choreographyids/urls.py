from django.urls import path
from . import views

urlpatterns = [
    path('', views.choreography_id_list, name='choreography_id_list'),
    path('create/', views.choreography_id_create, name='choreography_id_create'),
    path('<int:pk>/edit/', views.choreography_id_update, name='choreography_id_update'),
    path('<int:pk>/delete/', views.choreography_id_delete, name='choreography_id_delete'),
]
