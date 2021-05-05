from django.contrib import admin

# Register your models here.
from .models import house
from .models import organization

admin.site.register(house)
admin.site.register(organization)