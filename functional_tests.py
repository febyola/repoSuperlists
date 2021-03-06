from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	#def tearDown(self):
		#self.browser.quit()

	def test_can_start_a_list_and_retrive_it_later(self):
		self.browser.get('http://localhost:8000')
		
		self.assertIn('To-Do',self.browser.title)
		header_text = self.browser.find_element
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')
