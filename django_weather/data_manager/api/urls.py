from .views import LocationCreateView, LocationRUDView
from django.urls import path

urlpatterns = [
    path('location/<int:pk>', LocationRUDView.as_view(), name='location-rud'),  # location/<int:pk> specifies we're looking for a variable pk of type integer
    path('location/', LocationCreateView.as_view(), name='location-create'),  # name='xxx' specifies the django-friendly name of the URL
]


