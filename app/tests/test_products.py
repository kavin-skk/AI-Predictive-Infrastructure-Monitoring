import unittest
import requests


class TestProducts(unittest.TestCase):

    def test_products(self):

        response = requests.get("http://localhost:5000/products")

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()