from rest_framework import serializers
from data_manager.models import Location

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)  # This adds the url field to our model, that bears a URL to this data entry

    class Meta:
        model = Location  # Specifying the model we intend to serialize
        fields = ['url', 'country', 'state', 'city', 'longitude', 'latitude', ]  # Specifying what fields to be serialized

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)

