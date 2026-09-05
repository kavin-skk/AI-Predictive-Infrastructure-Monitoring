import unittest
import requests


class TestMetricsIntegration(unittest.TestCase):

    def test_metrics(self):

        response = requests.get("http://localhost:5000/metrics")

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()