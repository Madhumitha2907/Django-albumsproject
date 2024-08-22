from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('ticket/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/new/', views.ticket_new, name='ticket_new'),
    path('ticket/<int:pk>/edit/', views.ticket_edit, name='ticket_edit'),
    path('ticket/<int:pk>/delete/', views.ticket_delete, name='ticket_delete'),
]
