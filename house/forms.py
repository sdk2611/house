from django import forms

from .models import house

class HouseForm(forms.ModelForm):

    class Meta:
        model = house
        fields = ('title', 'houseguid', 'aoguid', 'management_org', 'house_type', 'housenum', 'buildnum', 'strucnum', 'eststatus', 'strstatus', 'cadnum', )