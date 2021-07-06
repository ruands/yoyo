from django.urls import path

from api.views import HealthCheckView, LocationWeatherView

urlpatterns = [
    # Locations
    path('locations/<str:city>/', LocationWeatherView.as_view()),
    # Healthcheck
    path('healthcheck/', HealthCheckView.as_view())
]
