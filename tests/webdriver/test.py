
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class Test(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def testSearchAtYouTube(self):
        self.browser.get('http://www.youtube.com')
        elem = self.browser.find_element_by_name('search_query')
        elem.send_keys('webdriver' + Keys.RETURN)
        time.sleep(0.2) # For now isn't in API.
        self.browser.find_element_by_css_selector('p.num-results')

    def testSearchAtGoogleImages(self):
        self.browser.get('http://images.google.com')
        elem = self.browser.find_element_by_name('q')
        elem.send_keys('webdriver' + Keys.RETURN)
        time.sleep(0.2) # For now isn't in API.
        self.browser.find_element_by_css_selector('div#resultStats')



if __name__ == '__main__':
    unittest.main()

