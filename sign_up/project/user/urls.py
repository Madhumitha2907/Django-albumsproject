from django.urls import path, include
from django.conf import settings
from user import views as user_view
from django.conf.urls.static import static
#from django.contrib.auth import views as 
from django.contrib.auth import views as auth_views




urlpatterns = [
		path('', user_view.index, name ='index'),
        path('login/', user_view.Login, name='login'),
        #path('logout/', auth.LogoutView.as_view(template_name='Index.html'), name='logout'),
        path('register/', user_view.register, name='register'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('logout/', user_view.custom_logout_view, name='logout'),

    
]
