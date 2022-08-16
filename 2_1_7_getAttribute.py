from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
 
    chest_treasure = browser.find_element(By.ID, "treasure")            # find the element that stores the "valuex"
    x = chest_treasure.get_attribute("valuex")                          # get_attribute
    y = calc(x)                                                         # calculate
    print(x)
    print(y)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')           # input the answer
    input1.send_keys(y)

    robox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')     # check the box
    robox.click()

    robtn = browser.find_element(By.CSS_SELECTOR, '#robotsRule')        # press the radiobutton
    robtn.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")        # Submit
    button.click()

finally:
    time.sleep(10)
    browser.quit()



