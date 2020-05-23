from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_home_page(self):
        # Go to site homepage
        self.browser.get('http://localhost:8000')

        # Check the site title
        self.assertIn('Jacob Wilson', self.browser.title)

        # Check the navbar
        headerText = self.browser.find_element_by_class_name('navbar-brand').text
        self.assertIn('Jacob', headerText)

        # Check for buttons for blog and cv
        nav = self.browser.find_elements_by_class_name('nav-link')
        self.assertTrue(any(link.text == 'Blog' for link in nav))
        self.assertTrue(any(link.text == 'CV' for link in nav))

        cards = self.browser.find_elements_by_class_name('card-title')
        self.assertTrue(any(title.text == 'Blog' for title in cards))
        self.assertTrue(any(title.text == 'CV' for title in cards))

if __name__ == '__main__':
    unittest.main(warnings='ignore')