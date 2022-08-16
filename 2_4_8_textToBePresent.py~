from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    expectedPrice = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )                                                       #check for 12 sec for the price to drop to $100

    button = browser.find_element(By.ID, "book")
    button.click()                                          #press the Book button
    

    fnum = browser.find_element(By.CSS_SELECTOR, "#input_value")    #get the value
    x = int(fnum.text)
    y = calc(x)                                                     #calculate
    print(x)
    print(y)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)                                             #input the value


    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")     #find the button
    button.click()                                                  #submit


finally:
    time.sleep(10)
    browser.quit()



