from django.urls import path
from .import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('forgot', views.forgot, name='forgot'),
    path('logout', views.logout, name='logout'),

   
]