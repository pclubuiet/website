from django.urls import resolve
from django.test import TestCase
import home.views as home_views

class ResourcePageTests(TestCase):
    def test_resourcepage_response_code(self):
        response = self.client.get('/home/resources/')
        self.assertEqual(response.status_code, 200)

    def test_resource_url_resolves_to_resourcepage_view(self):
        found = resolve('/home/resources/')
        self.assertEqual(found.func, home_views.ResourceView)
