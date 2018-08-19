from django.test import TestCase


class WebsiteTests(TestCase):

    def test_homepage(self):	#checks if homepage would be rendered properly
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_topicspage(self):	#checks if topics page would be rendered properly
        response = self.client.get('/home/topics/')
        self.assertEqual(response.status_code, 200)
