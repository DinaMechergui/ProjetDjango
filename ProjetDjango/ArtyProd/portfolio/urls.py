from . import views
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views 

urlpatterns =[
      path('', views.home, name="home"),
      path('register/', views.register, name='register'),
      path('accounts/', include('django.contrib.auth.urls')),
   
      path('register/',views.register, name = 'register'), 
      path('project/request/', views.project_request, name='project_request'),
    
    
   
]