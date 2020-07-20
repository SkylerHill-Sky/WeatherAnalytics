from rest_framework import serializers
from data_manager.models import Location

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['country', 'state', 'city', 'longitude', 'latitude', ]

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

