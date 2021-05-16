from django import forms
from django.utils import timezone
from django.forms import SelectDateWidget, TextInput
from .models import house

class HouseForm(forms.ModelForm):

    year = timezone.now().year
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = house
        exclude = ['created_date', 'author']
        # widgets = {
        #     'UsedYear': SelectDateWidget(attrs={'years': range(2021, -1)}),
        # }
    # UsedYear = forms.DateField(label = 'Дата ввода в эксплуатацию:', widget=forms.SelectDateWidget(years=range(year, year - 200, -1)))

class HouseFormView(forms.ModelForm):

    class Meta:
        model = house
        fields = '__all__'

    def __init__(self, *args, **kwargs): 
        super(HouseFormView, self).__init__(*args, **kwargs)                       
        self.fields['address'].widget.attrs['readonly'] = True
        self.fields['fullAddress'].widget.attrs['readonly'] = True
        self.fields['houseguid'].widget.attrs['readonly'] = True
        self.fields['UniqueNumber'].widget.attrs['readonly'] = True
        self.fields['aoguid'].widget.attrs['readonly'] = True
        self.fields['oktmo'].widget.attrs['readonly'] = True
        self.fields['housenum'].widget.attrs['readonly'] = True
        self.fields['buildnum'].widget.attrs['readonly'] = True
        self.fields['strucnum'].widget.attrs['readonly'] = True
        self.fields['house_type'].disabled = True
        self.fields['eststatus'].disabled = True
        self.fields['strstatus'].disabled = True
        self.fields['cadnum'].widget.attrs['readonly'] = True
        self.fields['TotalSquare'].widget.attrs['readonly'] = True
        self.fields['State'].disabled = True
        self.fields['LifeCycleStage'].disabled = True
        self.fields['UsedYear'].widget.attrs['readonly'] = True
        self.fields['FloorCount'].widget.attrs['readonly'] = True
        self.fields['UndergroundFloorCount'].widget.attrs['readonly'] = True
        self.fields['OlsonTZ'].widget.attrs['readonly'] = True
        self.fields['CulturalHeritage'].disabled = True
        self.fields['management_org'].disabled = True
        self.fields['created_date'].widget.attrs['readonly'] = True
        self.fields['author'].disabled = True

