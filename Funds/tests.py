from django.test import TestCase, Client
import unittest
# Create your tests here.


class FundPageLoad(TestCase):
    """ Test if the page is online"""
    def test_fund_load(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_charityPage(self):
        """ Test if page is being redirected"""
        response = self.client.get('/charityPage')
        self.assertEqual(response.status_code, 301)
