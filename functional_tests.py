from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

        self.browser.get('http://localhost:8000/accounts/login')
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('admin')
        password = self.browser.find_element_by_id('id_password')
        password.send_keys('testingAdmin')
        password.send_keys(Keys.ENTER)
        time.sleep(1)

    def tearDown(self):
        self.browser.get('http://localhost:8000/accounts/logout') 
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

    def test_cv_page(self):
        self.browser.get('http://localhost:8000/cv')

        # h1 element with my name
        name = self.browser.find_element_by_tag_name('h1')
        self.assertEqual('Jacob Wilson', name.text)

        # sections for education, skills, experience, projects and personal interests 
        headings = self.browser.find_elements_by_tag_name('h3')
        self.assertTrue(any(heading.text == 'Education' for heading in headings))
        self.assertTrue(any(heading.text == 'Skills' for heading in headings))
        self.assertTrue(any(heading.text == 'Experience' for heading in headings))
        self.assertTrue(any(heading.text == 'Projects' for heading in headings))
        self.assertTrue(any(heading.text == 'Personal Interests' for heading in headings))

    def test_cv_education(self):
        self.browser.get('http://localhost:8000/cv/new/education')

        # content to test
        title = 'School of life'
        subtitle = '2000 - Present'
        content = 'Doing okay hopefully'

        # find the submission elements
        titleBox = self.browser.find_element_by_id('id_ed_type')
        subtitleBox = self.browser.find_element_by_id('id_more_detail')
        contentBox = self.browser.find_element_by_id('id_content')
        saveButton = self.browser.find_element_by_class_name('save')

        # submit the content
        titleBox.send_keys(title)
        subtitleBox.send_keys(subtitle)
        contentBox.send_keys(content)
        saveButton.click()
        time.sleep(1)

        # check to see if content has been uploaded
        cards = self.browser.find_elements_by_class_name('card-body')
        self.assertTrue(any(title in card.text for card in cards))
        self.assertTrue(any(subtitle in card.text for card in cards))
        self.assertTrue(any(content in card.text for card in cards))

        # delete the inserted element
        for card in cards:
            if title in card.text:
                delete = card.find_element_by_tag_name('a')
                delete.click()
                time.sleep(1)
                break
        
        # check that the element has been deleted
        cards = self.browser.find_elements_by_class_name('card-body')
        self.assertFalse(any(title in card.text for card in cards))
        self.assertFalse(any(subtitle in card.text for card in cards))
        self.assertFalse(any(content in card.text for card in cards))

    def test_cv_skill(self):
        self.browser.get('http://localhost:8000/cv/new/skill')

        # content to test
        skill = 'Functional Testing'

        # find the submission elements
        contentBox = self.browser.find_element_by_id('id_content')
        techTick = self.browser.find_element_by_id('id_technical')
        saveButton = self.browser.find_element_by_class_name('save')

        # submit the content
        contentBox.send_keys(skill)
        techTick.click()
        saveButton.click()
        time.sleep(1)
        
        # check to see if the content has been uploaded
        skillsList = self.browser.find_element_by_id('technical-list')
        skills = self.browser.find_elements_by_class_name('list-group-item')
        self.assertTrue(any(skill in item.text for item in skills))

        # delete the inserted skill
        for item in skills:
            if skill in item.text:
                delete = item.find_element_by_tag_name('a')
                delete.click()
                time.sleep(1)
                break
        
        # check that the skill has been deleted
        skillsList = self.browser.find_element_by_id('technical-list')
        skills = skillsList.find_elements_by_class_name('list-group-item')
        self.assertFalse(any(skill in item.text for item in skills))

    def test_cv_experience(self):
        self.browser.get('http://localhost:8000/cv/new/experience')

        # content to test
        title = 'Life'
        subtitle = 'Permanent role - 2000-Present'
        content = 'Just the usual'

        # find the submission elements
        titleBox = self.browser.find_element_by_id('id_exp_type')
        subtitleBox = self.browser.find_element_by_id('id_more_detail')
        contentBox = self.browser.find_element_by_id('id_content')
        saveButton = self.browser.find_element_by_class_name('save')

        # submit the content
        titleBox.send_keys(title)
        subtitleBox.send_keys(subtitle)
        contentBox.send_keys(content)
        saveButton.click()
        time.sleep(1)

        # check to see if content has been uploaded
        cards = self.browser.find_elements_by_class_name('card-body')
        self.assertTrue(any(title in card.text for card in cards))
        self.assertTrue(any(subtitle in card.text for card in cards))
        self.assertTrue(any(content in card.text for card in cards))

        # delete the inserted element
        for card in cards:
            if title in card.text:
                delete = card.find_element_by_tag_name('a')
                delete.click()
                time.sleep(1)
                break
        
        # check that the element has been deleted
        cards = self.browser.find_elements_by_class_name('card-body')
        self.assertFalse(any(title in card.text for card in cards))
        self.assertFalse(any(subtitle in card.text for card in cards))
        self.assertFalse(any(content in card.text for card in cards))

    def test_cv_project(self):
        self.browser.get('http://localhost:8000/cv/new/project')

        # content to test
        title = 'This site'
        content = 'Developing and blog and CV website'

        # find the submission elements
        titleBox = self.browser.find_element_by_id('id_title')
        contentBox = self.browser.find_element_by_id('id_content')
        saveButton = self.browser.find_element_by_class_name('save')

        # submit the content
        titleBox.send_keys(title)
        contentBox.send_keys(content)
        saveButton.click()
        time.sleep(1)

        # check to see if content has been uploaded
        cards = self.browser.find_elements_by_class_name('card-body')
        self.assertTrue(any(title in card.text for card in cards))
        self.assertTrue(any(content in card.text for card in cards))

        # delete the inserted element
        for card in cards:
            if title in card.text:
                delete = card.find_element_by_tag_name('a')
                delete.click()
                time.sleep(1)
                break
        
        # check that the element has been deleted
        cards = self.browser.find_elements_by_class_name('card-body')
        self.assertFalse(any(title in card.text for card in cards))
        self.assertFalse(any(content in card.text for card in cards))

if __name__ == '__main__':
    unittest.main(warnings='ignore')