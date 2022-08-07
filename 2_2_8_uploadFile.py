from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
 

    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    input1.send_keys("John")

    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    input2.send_keys("Doe")

    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    input3.send_keys("john@doe.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))            # get the current path
    print(f"{current_dir}")

    file_path = os.path.join(current_dir, 'test_01.txt')                # add a filename to the current dir path

    input4 = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()                                                      #upload the file


finally:
    time.sleep(10)
    browser.quit()



