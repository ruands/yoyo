from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


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
    """

    def get(self, request, city, *args, **kwargs):
        return Response(city, status=200)
