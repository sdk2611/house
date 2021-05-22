from django.urls import path
from . import views
from .views import PremisesDeleteView

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('house/', views.house_list, name='house_list'),
    path('house/new/', views.house_new, name='house_new'),
    path('house/<int:pk>/', views.house_detail, name='house_detail'),
    path('house/<int:pk>/edit/', views.house_edit, name='house_edit'),
    path('house/<int:pk>/remove/', views.house_remove, name='house_remove'),
    path('premises/<int:house_id>/<int:entrance_id>/', views.premises_list, name='premises_list'),
    path('premises/<int:house_id>/<int:entrance_id>/new/', views.premises_new, name='premises_new'),
    path('premises/<int:house_id>/<int:entrance_id>/<int:pk>/edit/', views.premises_edit, name='premises_edit'),
    path('premises/<int:house_id>/<int:entrance_id>/<int:pk>/remove/', PremisesDeleteView.as_view(), name='premises_remove'),
    # path('premises/<int:house_id>/<int:entrance_id>/<int:pk>/remove/', views.premises_remove, name='premises_remove'),
]