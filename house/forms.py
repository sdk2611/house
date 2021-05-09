from django import forms
from django.utils import timezone

from .models import house

class HouseForm(forms.ModelForm):

    class Meta:
        model = house
        fields = '__all__'
    year = timezone.now().year
    UsedYear = forms.DateField(label = 'Дата ввода в эксплуатацию:', widget=forms.SelectDateWidget(years=range(year, year - 200, -1)))
