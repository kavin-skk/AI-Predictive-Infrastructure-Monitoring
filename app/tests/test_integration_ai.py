import unittest
import requests


class TestAIIntegration(unittest.TestCase):

    def test_ai_summary(self):

        response = requests.get("http://localhost:5000/ai-summary")

        self.assertEqual(response.status_code, 200)

        self.assertIn("success", response.json())


if __name__ == "__main__":
    unittest.main()