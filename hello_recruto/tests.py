from django.test import TestCase
from django.test import Client
import json
c = Client()
# Create your tests here.
class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_correct_data(self):
        response = c.get("/hello_recruto/", {"name": "Recruto", "message": "Давай дружить"})
        self.assertEquals(response.status_code, 200)

    def test_wrong_data(self):
        response = c.get("/hello_recruto/", {"name": "Recruto", "message": "Давай дружить"})
        self.assertEquals(response.status_code, 200)

    def test_wrong_url(self):
        response = c.get("/hello/", {"name": "Recruto", "message": "Давай дружить"})
        self.assertEquals(response.status_code, 404)