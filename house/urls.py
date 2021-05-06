from django.urls import path
from . import views

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
    path('house/new/', views.house_new, name='house_new'),
    path('house/<int:pk>/edit/', views.house_edit, name='house_edit'),
]