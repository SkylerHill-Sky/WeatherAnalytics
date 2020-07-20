from rest_framework import generics
from data_manager.models import Location
from .serializers import LocationSerializer
from django.views.decorators.csrf import csrf_exempt

class LocationCreateView(generics.ListCreateAPIView):  # ListCreateAPIView is a helpful mixin that gets us up and running fast.  For customization we can use GenericAPIView
    lookup_field = 'pk'  # url('# ?P<pk>\d+')
    serializer_class = LocationSerializer

    def get_queryset(self):
        qs = Location.objects.all()  # Define our queryset, in this case, all objects of type Location
        query = self.request.GET.get("q")  # Grab the query from the user
        if query is not None:
            qs = qs.filter(city__icontains=query)  # ...We'll need to re-work this query depending on what we want to be able to query based on
        return qs

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}  #

class LocationRUDView(generics.RetrieveUpdateDestroyAPIView):  # DetailView/RUDView
    lookup_field = 'pk'  # url('# ?P<pk>\d+')
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}