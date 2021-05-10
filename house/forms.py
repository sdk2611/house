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

class HouseFormView(forms.ModelForm):

    class Meta:
        model = house
        fields = '__all__'

    def __init__(self, *args, **kwargs): 
        super(HouseFormView, self).__init__(*args, **kwargs)                       
        self.fields['address'].disabled = True
        self.fields['fullAddress'].disabled = True
        self.fields['houseguid'].disabled = True
        self.fields['UniqueNumber'].disabled = True
        self.fields['aoguid'].disabled = True
        self.fields['oktmo'].disabled = True
        self.fields['housenum'].disabled = True
        self.fields['buildnum'].disabled = True
        self.fields['strucnum'].disabled = True
        self.fields['house_type'].disabled = True
        self.fields['eststatus'].disabled = True
        self.fields['strstatus'].disabled = True
        self.fields['cadnum'].disabled = True
        self.fields['TotalSquare'].disabled = True
        self.fields['State'].disabled = True
        self.fields['LifeCycleStage'].disabled = True
        self.fields['UsedYear'].disabled = True
        self.fields['FloorCount'].disabled = True
        self.fields['UndergroundFloorCount'].disabled = True
        self.fields['OlsonTZ'].disabled = True
        self.fields['CulturalHeritage'].disabled = True
        self.fields['management_org'].disabled = True
        self.fields['created_date'].disabled = True
        self.fields['author'].disabled = True

