from django.shortcuts import render

# Create your views here.
def house_list(request):
    return render(request, 'house/house_list.html', {})