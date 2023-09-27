import unittest
import json
from backend.app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()

    def tearDown(self):
        pass  # You can add cleanup code here if needed

    def test_parse_sql_endpoint(self):
        result = self._extracted_from_test_rebuild_sql_endpoint_3('/parse')
        self.assertTrue("ast" in result)

    def test_modify_sql_endpoint(self):
        result = self._extracted_from_test_rebuild_sql_endpoint_3('/modify')
        self.assertTrue("modified_ast" in result)
        self.assertTrue("mapping" in result)

    def test_rebuild_sql_endpoint(self):
        result = self._extracted_from_test_rebuild_sql_endpoint_3('/rebuild')
        self.assertTrue("rebuilded_sql" in result)

    # TODO Rename this here and in `test_parse_sql_endpoint`, `test_modify_sql_endpoint` and `test_rebuild_sql_endpoint`
    def _extracted_from_test_rebuild_sql_endpoint_3(self, endpoint):
        data = {"query": "SELECT a, b FROM test WHERE a = 5"}
        response = self.app.post(
            endpoint, data=json.dumps(data), content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        return json.loads(response.data)


if __name__ == '__main__':
    unittest.main()
