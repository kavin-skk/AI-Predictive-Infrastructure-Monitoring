import unittest
import requests


class TestHealthAPI(unittest.TestCase):

    def test_health(self):

        response = requests.get(
            "http://localhost:5000/health"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        data = response.json()

        self.assertEqual(
            data["status"],
            "Healthy"
        )


if __name__ == "__main__":

    unittest.main()