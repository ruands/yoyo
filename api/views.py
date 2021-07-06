import requests
import statistics

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from api import serializers
from api import utils


class HealthCheckView(APIView):
    """View to check status of API.
    """
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response(status=200)


class LocationWeatherView(APIView):
    """View for fetching the weather forecast for the specified city.
    
    Optional arguments:
    * Number of days

    Notes: weatherapi.com API Specifies 14-day forecast, sets the max to 10,
    but only returns the next 3 days. So not entirely sure what to believe.
    /history endpoint returns more data, but not useful as a forecast.
    """

    def get(self, request, city, *args, **kwargs):
        # Set days based on optional parameter, else 1
        days = request.GET.get("days", 1)

        # Set up external weather api url
        url = settings.WEATHER_API
        key = settings.WEATHER_API_KEY
        path = f'{url}/forecast.json?key={key}&q={city}&days={days}'

        # Make API call
        response = requests.get(path)

        if response.status_code == 200:
            # Pull only required data
            json_response = response.json()
            forecast = json_response.get("forecast", None)

            if forecast:
                temps = utils.get_temps_from_forecast(forecast)

                data = {
                    "maximum": max(temps),
                    "minimum": min(temps),
                    "average": utils.get_avg_temp(temps),
                    "median": statistics.median(temps)
                }

                serializer = serializers.LocationWeatherSerializer(data=data)
                if serializer.is_valid():
                    # Return forecast
                    return Response(serializer.validated_data, status=200)

             # If no 'forecast' key, we won't return data, so return 204.
            return Response(status=204)
        else:
            json_error = response.json()
            return Response(json_error.get("error").get("message"), status=response.status_code)
