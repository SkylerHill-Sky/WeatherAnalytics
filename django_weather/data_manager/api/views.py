from rest_framework import generics
from data_manager.models import Location
from .serializers import LocationSerializer
from django.views.decorators.csrf import csrf_exempt

class LocationCreateView(generics.ListCreateAPIView):
    lookup_field = 'pk' # url('# ?P<pk>\d+')
    serializer_class = LocationSerializer

    def get_queryset(self):
        qs = Location.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(name__icontains=query)
        return qs

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class LocationRUDView(generics.RetrieveUpdateDestroyAPIView): # DetailView
    lookup_field = 'pk' # url('# ?P<pk>\d+')
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}