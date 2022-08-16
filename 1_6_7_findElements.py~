from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type]')        #find_elements
    for element in elements:                                                #find all fields
        element.send_keys("response")                                       #fill in all fields

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")            #find submit button
    button.click()

finally:
    time.sleep(10)          # copy the code
    browser.quit()


