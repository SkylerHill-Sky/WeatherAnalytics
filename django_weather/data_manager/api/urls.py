from .views import LocationCreateView, LocationRUDView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('location/<int:pk>', LocationRUDView.as_view(), name='location-rud'),
    path('location/', LocationCreateView.as_view(), name='location-create'),
]


