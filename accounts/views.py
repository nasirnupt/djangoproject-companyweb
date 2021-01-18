from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Create your views here.
def register(request):
    return render(request, 'accounts/registration.html')

def login(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in Successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Username or Password!')
            return redirect('login')

    return render(request, 'accounts/login.html')


def forgot(request):
    return render(request, 'accounts/forgot.html')

def logout(request):

    context = {
        
    }
    return render(request, 'accounts/logout.html', context)
