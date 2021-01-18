from django.shortcuts import render
from.models import Slider
from.models import About
from.models import Client
from.models import Team
from.models import Testimonials




# Create your views here.
def index(request):
    slider_data = Slider.objects.all()
    about_data = About.objects.all()[0]
    client_data = Client.objects.all()


    context ={
        'slider': slider_data,
        'about':about_data,
        'client':client_data,
       
    }
    return render(request, 'pages/index.html', context)

def about(request):
    about_data = About.objects.all()[0]
    client_data = Client.objects.all()
    team_data = Team.objects.all()
    context ={
        'about':about_data,
        'client':client_data,
        'team':team_data,
    }
    return render(request, 'pages/about.html', context)

def team(request):
    team_data = Team.objects.all()

    context ={
        'team':team_data,
    }
    return render(request, 'pages/team.html', context)

def testimonials(request):
    testimonials_data = Testimonials.objects.all()

    context = {
        'testimonials':testimonials_data
    }
    return render(request, 'pages/testimonials.html', context)
