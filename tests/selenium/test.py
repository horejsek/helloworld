
import unittest
import selenium



class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium.selenium('localhost', 4444, '*firefox', 'http://localhost')
        self.selenium.start()

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

    def testSearchAtYouTube(self):
        self.selenium.open('http://www.youtube.com')
        self.selenium.type('search_query', 'selenium')
        self.selenium.click('search-btn')
        self.selenium.wait_for_page_to_load('30000')
        self.assertTrue(self.selenium.is_element_present('css=p.num-results'))

    def testSearchAtGoogleImages(self):
        self.selenium.open('http://images.google.com')
        self.selenium.type('q', 'selenium')
        self.selenium.click('btnG')
        self.selenium.wait_for_page_to_load('30000')
        self.assertTrue(self.selenium.is_element_present('css=div#resultStats'))



if __name__ == '__main__':
    unittest.main()

