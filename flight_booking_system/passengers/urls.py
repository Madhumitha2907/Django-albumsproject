# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.passenger_list, name='passenger_list'),
    path('passenger/<int:pk>/', views.passenger_detail, name='passenger_detail'),
    path('passenger/new/', views.passenger_new, name='passenger_new'),
    path('passenger/<int:pk>/edit/', views.passenger_edit, name='passenger_edit'),
   # path('passengers/passenger/new/', views.passenger_new, name='passenger_new'),
]
