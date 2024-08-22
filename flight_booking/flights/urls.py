from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('flight/new/', views.flight_new, name='flight_new'),  # Ensure this is before flight/<str:pk>/
    path('flight/<str:pk>/', views.flight_detail, name='flight_detail'),
    path('flight/<str:pk>/edit/', views.flight_edit, name='flight_edit'),
    path('flight/<str:pk>/delete/', views.flight_delete, name='flight_delete'),
    path('flights/', views.flights_view, name='flights'),
]
