from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse

# Location model

class Location(models.Model):

    cUS = 'US' # c = Country, so cUS = Country USA
    cCA = 'CA'

    COUNTRY_LIST = [
        (cUS, 'United States'),
        (cCA, 'Canada'),
    ]

    country = models.CharField( # CharField with predefined choices
        max_length=2,
        choices=COUNTRY_LIST,
        default=cUS,
    )

    sTX = 'US'
    sCA = 'CA' # s = State, so sCA = State California

    STATE_LIST = [
        (sTX, 'Texas'),
        (sCA, 'California'),
    ]

    state = models.CharField(
        max_length=2,
        choices=STATE_LIST,
        default=sTX,
    )

    city = models.CharField(max_length=20)
    longitude = models.FloatField(max_length=20)
    latitude = models.FloatField(max_length=20)

    def __str__(self):
        return self.city # Maybe should do something else here...  Multiple lat+long per city

    def get_api_url(self, request=None):
        return api_reverse("api:customer-rud", kwargs={'pk': self.pk}, request=request)

class DailyTemp(models.Model):
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    date = models.DateField()
    day_temp = models.IntegerField()
    hourly_temp_array = ArrayField(models.IntegerField())

    def __str__(self):
        return "dailytemp" # Not sure what to do for this one

    def get_api_url(self, request=None):
        return api_reverse("api:customer-rud", kwargs={'pk': self.pk}, request=request)
