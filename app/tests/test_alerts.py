import unittest
import requests


class TestAlerts(unittest.TestCase):

    def test_alerts(self):

        response = requests.get(
            "http://localhost:5000/alerts"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        data = response.json()

        self.assertTrue(
            data["success"]
        )


if __name__ == "__main__":

    unittest.main()