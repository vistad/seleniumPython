from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
 
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()                                              # press the button to redirect to the new page

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)                        # switch to the new tab

    fnum = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(fnum.text)
    y = calc(x)
    print(x)
    print(y)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")    # submit 
    button.click()


finally:
    time.sleep(10)
    browser.quit()



