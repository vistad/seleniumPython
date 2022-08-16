from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
 
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")    #find the button
    button.click()                                                  #click the button
    time.sleep(2)

    confirm = browser.switch_to.alert                               #switch_to.alert
    confirm.accept()                                                #confirm.accept OK

    fnum = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(fnum.text)
    y = calc(x)                                                     #calculate the value
    print(x)
    print(y)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')       #find the input
    input1.send_keys(y)                                             #input the value


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()                                                  #submit


finally:
    time.sleep(10)
    browser.quit()



