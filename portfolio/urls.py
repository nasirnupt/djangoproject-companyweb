from django.urls import path
from .import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfoliodetails, name='portfolio-details'),
   
]