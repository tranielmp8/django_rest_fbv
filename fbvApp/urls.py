from django.urls import path
from . import views

urlpatterns = [
    path('passengers/', views.passenger_list, name='passenger_list'),
    path('passengers/<int:pk>', views.passenger_detail, name='passenger_list')
]
