from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('reservation/<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('reservation/new/', views.reservation_new, name='reservation_new'),
    path('reservation/<int:pk>/edit/', views.reservation_edit, name='reservation_edit'),
]
