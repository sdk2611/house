from django.shortcuts import render, get_object_or_404
from .models import house
from django.utils import timezone

# Create your views here.
def house_list(request):
    houses = house.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'house/house_list.html', {'houses' : houses})

def house_detail(request, pk):
    _house = get_object_or_404(house, pk=pk)
    return render(request, 'house/house_detail.html', {'house' : _house})
