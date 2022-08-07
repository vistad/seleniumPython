from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    print(x)
    print(y)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    robox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')     #click the checkbox 
    robox.click()

    robtn = browser.find_element(By.CSS_SELECTOR, '#robotsRule')     #click the radiobutton 
    robtn.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")     #submit the form
    button.click()


finally:
    time.sleep(10)
    browser.quit()



