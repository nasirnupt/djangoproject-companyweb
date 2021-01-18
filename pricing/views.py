from django.shortcuts import render
from.models import Pricing

# Create your views here.
def pricing(request):
    pricing_data = Pricing.objects.all()

    context ={
        'pricing':pricing_data,
    }

    return render(request, 'pricing/pricing.html', context)