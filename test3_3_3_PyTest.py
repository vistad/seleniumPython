#a few tests in the test-suite
#passes test_registration1
#fails test_registration2


from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import pytest


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        browser.implicitly_wait(2)                  #wait for page to load
        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('John')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Doe')
        browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('11111@email.com')
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")      #find the webelement with the text
        welcome_text = welcome_text_elt.text        #store webelement text to the var            
        assert"Congratulations! You have successfully registered!", welcome_text
        browser.quit()



    def test_registration2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        browser.implicitly_wait(2)                  #wait for page to load
        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('John')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Doe')
        browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('11111@email.com')
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")      #find the webelement with the text
        welcome_text = welcome_text_elt.text        #store webelement text to the var            
        assert"Congratulations! You have successfully registered!", welcome_text
        browser.quit()

        
if __name__ == "__main__":
    pytest.main()



