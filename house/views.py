from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import house
from .forms import HouseForm

# Create your views here.
def house_list(request):
    houses = house.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'house/house_list.html', {'houses' : houses})

def house_detail(request, pk):
    _house = get_object_or_404(house, pk=pk)
    return render(request, 'house/house_detail.html', {'house' : _house})

def house_new(request):
    if request.method == "POST":
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.author = request.user
            house.created_date = timezone.now()
            house.save()
            return redirect('house_detail', pk=house.pk)
    else:
        form = HouseForm()
    return render(request, 'house/house_edit.html', {'form': form})

def house_edit(request, pk):
    _house = get_object_or_404(house, pk=pk)
    if request.method == "POST":
        form = HouseForm(request.POST, instance=_house)
        if form.is_valid():
            _house = form.save(commit=False)
            _house.author = request.user
            _house.created_date = timezone.now()
            _house.save()
            return redirect('house_detail', pk=_house.pk)
    else:
        form = HouseForm(instance=_house)
    return render(request, 'house/house_edit.html', {'form': form})