"Test for Api"
import logging
import unittest
import requests
import json

logging.basicConfig(
    filename="test.log", level=logging.INFO, format="%(levelname)s:%(message)s"
)

class TestApi(unittest.TestCase):
    "Class to test Api"
    def test_api(self):
        "Tests for the api"
        url = "https://corona-virus-stats.herokuapp.com/api/v1/cases" \
              "/countries-search?search=netherlands"
        test = requests.get(url)
        status_code = test.status_code
        expected = 200
        data = test.json()
        logging.info("Json Data" + str(data))


        status = data["status"]
        status_message = "success"

        self.assertEqual(status_code, expected)
        self.assertEqual(status, status_message)


if __name__ == '__main__':
    unittest.main()
