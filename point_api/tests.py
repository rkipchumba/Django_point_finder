from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class PointAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_find_closest_points(self):
        data = {
            "points": "2,2;-1,30;20,11;4,5"
        }
        response = self.client.post('/api/closest-points/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['closest_points'], '2,2;4,5')
