import unittest
import requests


class TestAlertsIntegration(unittest.TestCase):

    def test_alerts(self):

        response = requests.get("http://localhost:5000/alerts")

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.json()["success"])


if __name__ == "__main__":
    unittest.main()