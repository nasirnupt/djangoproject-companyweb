from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_data = Contact(name=name, email=email, subject=subject,message=message)
        contact_data.save()

        messages.success(request, 'Your message has been sent successfully, Thanks!')


    return render(request, 'contacts/contact.html')

