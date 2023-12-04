import os
import unittest
from urllib.request import urlopen
import http.client
import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # en segundos

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_subtract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        result = response.read().decode('utf-8')
        self.assertEqual(result, '2')

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/4/6"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        result = response.read().decode('utf-8')
        self.assertEqual(result, '24')

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/8/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        result = response.read().decode('utf-8')
        self.assertEqual(result, '4.0')

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        result = response.read().decode('utf-8')
        self.assertEqual(result, '8')

    def test_api_raiz_cuadrada(self):
        url = f"{BASE_URL}/calc/raiz_cuadrada/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        result = response.read().decode('utf-8')
        self.assertEqual(result, '4.0')

    def test_api_logaritmo_base_10(self):
        url = f"{BASE_URL}/calc/logaritmo_base_10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        result = response.read().decode('utf-8')
        self.assertEqual(result, '2.0')

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
