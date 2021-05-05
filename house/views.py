from django.shortcuts import render
from .models import house
from django.utils import timezone

# Create your views here.
def house_list(request):
    houses = house.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'house/house_list.html', {'houses' : houses})