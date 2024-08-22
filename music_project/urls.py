"""
URL configuration for music_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Albums.views import home  # Ensure the home view is correctly imported

urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('albums/', include('Albums.urls')),
    path('songs/', include('Songs.urls')),
    path('choregraphydetails/', include('choreographydetails.urls')),
    path('songwriters/', include('SongWriters.urls')),
    path('songsingers/', include('SongSingers.urls')),
    path('choregraphyids/', include('choreographyids.urls')),
    path('singers/', include('Singers.urls')),
    path('writers/', include('Writers.urls')),
    

]
