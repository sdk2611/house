from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import house, ResidentialPremises
from .forms import HouseForm, HouseFormView
from .forms import PremisesForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db.models import F, Q
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here. 
def main_page(request):
    return render(request, 'main.html')

def house_list(request):
    houses = house.objects.all()
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
        premises = ResidentialPremises.objects.extra(
            select={'myinteger': 'CAST(PremisesNum AS INTEGER)'}
            ).order_by('myinteger')
    else:
        premises = ResidentialPremises.objects.filter(Q(house = house_id), Q(Entrance = entrance_id) | Q(Entrance = None)).extra(
            select={'myinteger': 'CAST(PremisesNum AS INTEGER)'}
            ).order_by('myinteger')
    paginator = Paginator(premises, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # return render(request, 'premises/premises_list.html', {'page_obj': page_obj})
    return render(request, 'premises/premises_list.html', context={'page_obj': page_obj, 'house': house_id, 'entrance' : entrance_id})

@login_required
def premises_new(request, house_id, entrance_id):
    if request.method == "POST":
        form = PremisesForm(request.POST)
        if form.is_valid():
            premises = form.save(commit=False)
            premises.author = request.user
            premises.created_date = timezone.now()
            premises.save()
            return redirect('premises_list', house_id=house_id, entrance_id= entrance_id)
    else:
        form = PremisesForm(initial = {'house' : house_id})
    return render(request, 'premises/premises_edit.html', {'form': form})

@login_required
def premises_edit(request, house_id, entrance_id, pk):
    _premises = get_object_or_404(ResidentialPremises, pk=pk)
    if request.method == "POST":
        form = PremisesForm(request.POST, instance=_premises)
        if form.is_valid():
            _premises = form.save(commit=False)
            _premises.author = request.user
            _premises.created_date = timezone.now()
            _premises.save()
            return redirect('premises_list', house_id=house_id, entrance_id=entrance_id)
    else:
        form = PremisesForm(instance=_premises)
    return render(request, 'premises/premises_edit.html', {'form': form})

@login_required
def premises_remove(request, house_id, entrance_id, pk):
    _premises = get_object_or_404(ResidentialPremises, pk=pk)
    _premises.delete()
    return redirect('premises_list', house_id=house_id, entrance_id=entrance_id)

class PremisesDeleteView(DeleteView):
    # specify the model you want to use
    model = ResidentialPremises
     
    # can specify success url
    # url to redirect after sucessfully
    # deleting object
    def get_success_url(self):
        return reverse_lazy('premises_list',kwargs={'house_id': self.object.house.pk, 'entrance_id': 0})
    # success_url = reverse_lazy('premises_list', kwargs={'house_id': self.object.house.pk, 'entrance_id': self.object.entrance.pk})