from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)                  #wait for page to load

    button = browser.find_element(By.ID, "verify")
    #or button = browser.find_element(By.CSS_SELECTOR, ".btn#verify")
    time.sleep(2)
    button.click()                                   # press the button

    message = browser.find_element(By.ID, "verify_message")    #find the verify_message
    assert "successful" in message.text


finally:
    time.sleep(2)
    browser.quit()



