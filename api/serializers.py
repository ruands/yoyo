from rest_framework import serializers


class LocationWeatherSerializer(serializers.Serializer):
    maximum = serializers.DecimalField(max_digits=4, decimal_places=2)
    minimum = serializers.DecimalField(max_digits=4, decimal_places=2)
    average = serializers.DecimalField(max_digits=4, decimal_places=2)
    median = serializers.DecimalField(max_digits=4, decimal_places=2)
