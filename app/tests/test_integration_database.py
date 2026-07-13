import unittest
import requests


class TestDatabaseIntegration(unittest.TestCase):

    def test_database_connection(self):

        response = requests.get("http://localhost:5000/dbtest")

        self.assertEqual(response.status_code, 200)

        self.assertIn("status", response.json())


if __name__ == "__main__":
    unittest.main()