from django.urls import path
from . import views

urlpatterns = [
    path('', views.choreography_detail_list, name='choreography_detail_list'),
    path('create/', views.choreography_detail_create, name='choreography_detail_create'),
    path('<int:pk>/edit/', views.choreography_detail_update, name='choreography_detail_update'),
    path('<int:pk>/delete/', views.choreography_detail_delete, name='choreography_detail_delete'),
]
