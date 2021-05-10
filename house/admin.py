from django.contrib import admin

# Register your models here.
from .models import house
from .models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportMixin

class HouseResource(resources.ModelResource):
    class Meta:
        model = house

class HouseAdmin(ImportExportModelAdmin):
    resource_class = HouseResource
    pass

admin.site.register(organization)
admin.site.register(house, HouseAdmin)

