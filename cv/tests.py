from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from cv.views import cv_page

class HomePageTest(TestCase):
    def test_cv_page_returns_correct_html(self):
        # request = HttpRequest()
        response = self.client.get('/cv/')
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<!doctype html>'))
        self.assertIn("<title>Jacob Wilson's Blog", html)
        self.assertTrue(html.endswith('</html>'))
        
        self.assertTemplateUsed(response, 'cv/cv.html')