from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import house, ResidentialPremises
from .forms import HouseForm, HouseFormView
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db.models import F, Q

# Create your views here. 
def main_page(request):
    return render(request, 'main.html')

def house_list(request):
    houses = house.objects.order_by('address')
    paginator = Paginator(houses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'house/house_list.html', {'page_obj': page_obj})

def house_detail(request, pk):
    _house = get_object_or_404(house, pk=pk)
    _form = HouseFormView(instance=_house)
    return render(request, 'house/house_detail.html', context={'form': _form, 'house': _house})

@login_required
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

@login_required
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

@login_required
def house_remove(request, pk):
    _house = get_object_or_404(house, pk=pk)
    _house.delete()
    return redirect('house_list')

def premises_list(request, house_id, entrance_id):
    if house_id == 0:
        premises = ResidentialPremises.objects.order_by('PremisesNum')
    else:
        premises = ResidentialPremises.objects.filter(Q(house = house_id), Q(Entrance = entrance_id) | Q(Entrance = None)).order_by('PremisesNum')
    paginator = Paginator(premises, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'premises/premises_list.html', {'page_obj': page_obj})
