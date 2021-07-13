from unittest.mock import patch

from django.test import TestCase


class LocationWeatherViewTestCase(TestCase):

    def expected_result(*args, **kwargs):
        return {
            "forecast": {
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
        }

    def empty_result(*args, **kwargs):
        return {
            "forecast": {
                "forecastday": []
            }
        }

    def no_content_result(*args, **kwargs):
        return {}

    def error_result(*args, **kwargs):
        return {
            "error": {
                "code": 1002,
                "message": "API key is invalid or not provided."
            }
        }

    @patch('requests.get')
    def test_200_response_with_default_temps(self, mock_get):
        # Test an expected 200 response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = self.empty_result()

        response = self.client.get(
            f"/api/locations/johannesburg/"
        )
        content = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(content["maximum"], 0)
        self.assertEqual(content["minimum"], 0)
        self.assertEqual(content["average"], 0)
        self.assertEqual(content["median"], 0)

    @patch('requests.get')
    def test_200_response(self, mock_get):
        # Test an expected 200 response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = self.expected_result()

        response = self.client.get(
            f"/api/locations/johannesburg/"
        )
        content = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(content["maximum"], 25)
        self.assertEqual(content["minimum"], 15)
        self.assertEqual(content["average"], 20)
        self.assertEqual(content["median"], 20)


    @patch('requests.get')
    def test_204_response(self, mock_get):
        # Test a response that has no content
        mock_get.return_value.status_code = 200  # The external API returns 200
        mock_get.return_value.json.return_value = self.no_content_result()

        response = self.client.get(
            f"/api/locations/johannesburg/"
        )

        self.assertEqual(response.status_code, 204)

    @patch('requests.get')
    def test_error_response(self, mock_get):
        # Test a response that has no content
        mock_get.return_value.status_code = 401
        mock_get.return_value.json.return_value = self.error_result()

        response = self.client.get(
            f"/api/locations/johannesburg/"
        )

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), "API key is invalid or not provided.")
