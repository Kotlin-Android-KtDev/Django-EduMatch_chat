from selenium import webdriver
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_using_chat_app(self):  
        # Antony want to chat with his friend and he heard their have a new web chat. 
        # He go to check out this web .
        self.browser.get('http://127.0.0.1:8000/chat')

        # He notices the page title and header mention to-do lists
        self.assertIn('Edu-Match', self.browser.title) 

        #He want to chat with his friend ,so he type name of his friend group and pressed enter to join the chat .
        search_box = self.browser.find_element_by_id('room-name-input')
        submit_button = self.browser.find_element_by_id('room-name-submit')
        search_box.send_keys('Cpr.E 16')

        
        self.fail('Finish the test!')