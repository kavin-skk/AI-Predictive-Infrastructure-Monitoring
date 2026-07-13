import unittest
import requests


class TestAISummary(unittest.TestCase):

    def test_summary(self):

        response = requests.get(
            "http://localhost:5000/ai-summary"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        data = response.json()

        self.assertTrue(
            "success" in data
        )


if __name__ == "__main__":

    unittest.main()