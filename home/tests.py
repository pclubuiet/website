from django.test import TestCase


class WebsiteTests(TestCase):

    def test_homepage(self):	#checks if homepage would be rendered properly
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_resourcepage(self):	#checks if resources page would be rendered properly
        response = self.client.get('/resources/')
        self.assertEqual(response.status_code, 200)
