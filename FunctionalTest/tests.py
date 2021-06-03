from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):



	def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('list_table')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
      	               raise e                  
                   time.sleep(0.5)  
                 
	def setUp(self):
	 	self.browser = webdriver.Firefox()

	def test_browser_title(self):
	 	self.browser.get(self.live_server_url)
	 	self.assertIn('ECT Application',self.browser.title)
	 	header_text = self.browser.find_element_by_tag_name('h1').text
	 	self.assertIn('Welcome to ECT Application!', header_text)

	 	fname = self.browser.find_element_by_id('fname')
	 	self.assertEqual(fname.get_attribute('placeholder'), "Full Name")
	 	fname.click()
	 	fname.send_keys('Micah Tugas')
	 	time.sleep(1)
    
	 	depname = self.browser.find_element_by_id('depname')
	 	self.assertEqual(depname.get_attribute('placeholder'), "Department")
	 	depname.click()
	 	depname.send_keys('Production Department')
	 	time.sleep(1)

	 	btnContinue = self.browser.find_element_by_id('btnContinue')
	 	btnContinue.click()
	 	time.sleep(2)
      
	 	kaddress = self.browser.find_element_by_id('kaddress')
	 	self.assertEqual(kaddress.get_attribute('placeholder'), "Complete Address")
	 	kaddress.click()
	 	kaddress.send_keys('Sta.Lucia Dasma')
	 	time.sleep(1)
     
	 	Reason = self.browser.find_element_by_id('Reason')
	 	self.assertEqual(Reason.get_attribute('placeholder'), "Purpose")
	 	Reason.click()
	 	Reason.send_keys('Employment')
	 	time.sleep(1)
     
	 	info = self.browser.find_element_by_id('info')
	 	self.assertEqual(info.get_attribute('placeholder'), "Number")
	 	info.click()
	 	info.send_keys('0916375948126')
	 	time.sleep(1)

	 	sdate = self.browser.find_element_by_id('sdate')
	 	sdate.click()
	 	sdate.send_keys('2000-09-06')
	 	time.sleep(1)

	 	sign1 = self.browser.find_element_by_id('sign1')
	 	sign1.click()
	 	sign1.send_keys('none')
	 	time.sleep(1)
     
	 	btnConfirm = self.browser.find_element_by_id('btnConfirm')
	 	btnConfirm.click()
	 	time.sleep(2)
     


    
if __name__=='__main__':
        unittest.main()