from django.urls import path
from main.views import index,about,welcome, contactus, contact, logout_view, ayuda
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index,name="index"),
    path('about/', about, name="about"),
    path('welcome/', welcome, name="welcome"),
    path('contact/', contact, name="contact"),
    path('contactus/', contactus, name="contactus"),
    path('logout/', logout_view, name='logout'), 
    path('help/', ayuda, name="help"),
]
