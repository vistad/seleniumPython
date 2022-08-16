from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"        # should fail on this page
    # link = "http://suninjuly.github.io/registration1.html"      # should pass on this page
    browser = webdriver.Chrome()
    browser.get(link)

    # find and fill in the fields
    browser.find_element(By.CSS_SELECTOR, ".first_block > div.form-group.first_class > input.form-control.first").send_keys('Test_name')
    browser.find_element(By.CSS_SELECTOR, ".first_block > div.form-group.second_class > input.form-control.second").send_keys('Test_name')
    browser.find_element(By.CSS_SELECTOR, ".first_block > div.form-group.third_class > input.form-control.third").send_keys('Test_name')

    # Submit the form
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)       # wait for the page to load
    
    # check if the registration is successful
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")      # find the webelement with the text
    welcome_text = welcome_text_elt.text        # store webelement text to the var

    assert "Congratulations! You have successfully registered!" == welcome_text     # check the expected text is equal to the present text

finally:
    time.sleep(10)
    browser.quit()
