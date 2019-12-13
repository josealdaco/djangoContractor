import unittest
from django.test import TestCase, Client
import requests

# Create your tests here.


class PageAPIViewer(TestCase):
    """ Check if API is getting data"""
    def test_pageAPI(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_API(self):
        """ Test that API is working properly, no 404"""
        response = requests.get('https://charitywebsite.herokuapp.com/api/pages/?format=json')
        self.assertEqual(response.status_code, 200)
