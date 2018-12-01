from app import create_app
import unittest
import json

app = create_app()

class TestUsers(unittest.TestCase):

    def setUp(self):
        app.testing = True 
        self.app = app.test_client()
        self.data = {
        "createdBy": "oceans",
        "createdOn": "05/12/2018",
        "description": "There has been some...",
        "image": "image",
        "location": "Mombasa",
        "status": "Draft",
        "title": "Maize-Scandal",
        "type": "Red-Flag",
        "video": "video"
        }

    def test_redflag_get(self):
        response = self.app.get('/api/v1/redflags')
        self.assertEqual(response.status_code, 200)

    def test_redflag_post(self):
        response = self.app.post('api/v1/redflags', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_redflag_patch(self):
        response = self.app.patch('api/v1/redflags/2', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_redflag_delete(self):
        response = self.app.delete('api/v1/redflags/1', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_redflag_get_one(self):
        response = self.app.get('api/v1/redflags/2', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.data = {}

if __name__ == '__main__':
    unittest.main()