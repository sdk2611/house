from django.contrib import admin

# Register your models here.
from .models import *

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin, ImportMixin

class HouseResource(resources.ModelResource):
    class Meta:
        model = house

class HouseAdmin(ImportExportModelAdmin):
    resource_class = HouseResource
    pass

class ResidentialPremisesResource(resources.ModelResource):
    house = fields.Field(
        column_name='house',
        attribute='house',
        widget=ForeignKeyWidget(house, 'houseguid'))
    class Meta:
        model = ResidentialPremises

class ResidentialPremisesAdmin(ImportExportModelAdmin):
    resource_class = ResidentialPremisesResource
    pass

admin.site.register(organization)
admin.site.register(house, HouseAdmin)
admin.site.register(ResidentialPremises, ResidentialPremisesAdmin)

