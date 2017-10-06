from django.urls import resolve
from django.test import TestCase
import home.views as home_views


class HomePageTests(TestCase):
    def test_homepage_response_code(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_to_homepage_view(self):
        found = resolve('/home/')
        self.assertEqual(found.func, home_views.HomeView)
