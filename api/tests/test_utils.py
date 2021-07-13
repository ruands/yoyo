from django.test import TestCase

from api.utils import get_avg_temp, get_temps_from_forecast


class UtilTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.forecast = {
            "forecastday": [
                {
                    "hour": [
                        {
                            "temp_c": 25
                        },
                        {
                            "temp_c": 15
                        }
                    ]
                }
            ]
        }

        cls.forecast_empty = {
            "forecastday": [
                {
                    "hour": [
                    ]
                }
            ]
        }

    def test_temps_from_forecast(self):
        temps = get_temps_from_forecast(self.forecast)
        self.assertEqual(temps, [25, 15])

    def test_empty_temps(self):
        temps = get_temps_from_forecast(self.forecast_empty)
        self.assertEqual(temps, [])

    def test_avg_temp_calculation(self):
        temps = get_temps_from_forecast(self.forecast)
        average = get_avg_temp(temps)
        self.assertEqual(average, 20)

    def test_avg_no_temps(self):
        temps = get_temps_from_forecast(self.forecast_empty)
        average = get_avg_temp(temps)
        self.assertEqual(average, 0)
