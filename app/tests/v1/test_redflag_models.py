from app import create_app
import unittest
import json


app = create_app()

class TestUsers(unittest.TestCase):

    def setUp(self):
        app.testing = True 
        self.app = app.test_client()
        self.dt = {
            "createdBy" : "John",
            "location" : "Malindi",
            "title" : "Corruption"
        }
    def test_redflag_get_empty(self):
        response = self.app.get('/api/v1/redflags')
        self.assertEqual(response.status_code, 200)

    def test_redflag_get(self):
        response = self.app.post('api/v1/redflags', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.get('api/v1/redflags', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result["Status"], 200)

    def test_redflag_post(self):
        response = self.app.post('api/v1/redflags', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'RedFlag added successfully.')

    def test_redflag_patch(self):
        response = self.app.post('api/v1/redflags', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.patch('api/v1/redflags/1', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Change made successfully.')

    def test_redflag_patch_nonexisting(self):
        response = self.app.post('api/v1/redflags', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 201)  
        response = self.app.patch('api/v1/redflags/4', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data)
        self.assertEqual(result["Error"], "RedFlag does not exist.")

    def test_redflag_delete(self):
        response = self.app.post('api/v1/redflags', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.app.delete('api/v1/redflags/1', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_redflag_delete_nonexisting(self):
        response = self.app.delete('api/v1/redflags/3', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 404)


    def test_redflag_get_one(self):
        response = self.app.get('api/v1/redflags/1', data=json.dumps(self.dt), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_redflag_get_one_nonexisting(self):
        response = self.app.get('api/v1/redflags/3')
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
