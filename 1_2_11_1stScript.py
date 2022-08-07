from selenium import webdriver      # webdriver - a set of commands to control a brwoser
from selenium.webdriver.common.by import By     # import class By that enables usage of different search methods
import time     # time management


driver = webdriver.Chrome()     # initialization of browser driver that starts the new browser instance

time.sleep(5)       # command time.sleep sets a 5 sec pause to let us see what's going on

driver.get("https://stepik.org/lesson/25969/step/12")       # open the address
time.sleep(5)

textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")        # method find_element finds an element using a selector and a value

textarea.send_keys("get()")     # we write text to the input we found
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")      # search for a submit button

submit_button.click()       # click the submit button
time.sleep(5)

driver.quit()       # close the window


