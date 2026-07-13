import unittest
import requests


class TestCheckout(unittest.TestCase):

    def test_checkout(self):

        response = requests.get("http://localhost:5000/checkout")

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()