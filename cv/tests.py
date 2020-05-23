from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from cv.views import cv_page

class HomePageTest(TestCase):
    def test_cv_url_resolves_to_cv_page_view(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_page)

    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn("<title>Jacob Wilson's Blog", html)
        self.assertTrue(html.endswith('</html>'))
