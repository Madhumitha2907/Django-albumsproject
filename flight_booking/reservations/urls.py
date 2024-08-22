from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('reservation/<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('reservation/new/', views.reservation_new, name='reservation_new'),
    path('reservation/<int:pk>/edit/', views.reservation_edit, name='reservation_edit'),
    path('reservation/<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),
    path('reservation/create/', views.create_reservation, name='create_reservation'),
    path('reservation/cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
     path('reservations/', views.reservations_view, name='reservations'),
]
