#a few tests in the test-suite
#passes test_registration1
#fails test_registration2


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

try: 
    browser = webdriver.Chrome()

    class TestRegistration(unittest.TestCase):
        def test_registration1(self):
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')        # fill in the fields
            input1.send_keys('John')
            input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
            input2.send_keys('Doe')
            input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
            input3.send_keys('11111@email.com')
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)           # wait for the page to load
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")          # find the text
            welcome_text = welcome_text_elt.text            # write the text from element welcome_text_elt to the var welcome_text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be same text")



        def test_registration2(self):
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)
            browser.find_element(By.CSS_SELECTOR, ".first_block > div.form-group.first_class > input.form-control.first").send_keys('Test_name')
            browser.find_element(By.CSS_SELECTOR, ".first_block > div.form-group.second_class > input.form-control.second").send_keys('Test_name')
            browser.find_element(By.CSS_SELECTOR, ".first_block > div.form-group.third_class > input.form-control.third").send_keys('Test_name')
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()            #Submit the form
            time.sleep(1)       #wait for the page to load
            #check if the registration is successful
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")      #find the webelement with the text
            welcome_text = welcome_text_elt.text        #store webelement text to the var
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be same text")

            
    if __name__ == "__main__":
        unittest.main()

finally:
    time.sleep(5)
    browser.quit()

