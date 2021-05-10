from django import forms
from django.utils import timezone
from django.forms import SelectDateWidget
from .models import house

class HouseForm(forms.ModelForm):

    year = timezone.now().year
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = house
        exclude = ['created_date', 'author']
    #        widgets = {
#            'UsedYear': SelectDateWidget(attrs={'years': range(2021, , -1)}),
#        }
    UsedYear = forms.DateField(label = 'Дата ввода в эксплуатацию:', widget=forms.SelectDateWidget(years=range(year, year - 200, -1)))
