import unittest
import json

from pythoncode import app

BASE_URL = "http://46.101.202.234:8000/numbers/7"
ERROR_URL = "http://46.101.202.234:8000/numbers/-7" ## Intentionallly send bad param

class TestFlaskApi(unittest.TestCase):

	## Prapare app for testing
	## With everything that might be necessary
	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True

	def test_http_response_and_fib_minimal(self):

		good_response = self.app.get(BASE_URL)
		self.assertEqual(good_response.status_code, 200) ## Expect 200 for a valid http response

		data = json.loads(good_response.get_data().decode('utf-8'))
		self.assertEqual(len(data), 7) ## Expect list of 7 items as a Fibonacci API response to /7 request

		bad_response = self.app.get(ERROR_URL)
		message = json.loads(bad_response.get_data().decode('utf-8'))
		self.assertEqual(message["error"], "Invalid value - please pass a possitive number") ## Expect list of 7 items as a Fibonacci API response to /7 request

	## End tests
	## Unset anything that is no longer required
	def tearDown(self):
		self.app.testing = False

if __name__ == "__main__":
	unittest.main()