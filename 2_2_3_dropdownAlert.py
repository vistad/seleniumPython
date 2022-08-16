from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def sum(x, y):
    return str(x + y)


try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    fnum = browser.find_element(By.CSS_SELECTOR, "#num1")
    snum = browser.find_element(By.CSS_SELECTOR, "#num2")

    x = int(fnum.text)
    y = int(snum.text)
    z = sum(x, y)                                           # add numbers
    print(x)
    print(y)
    print(z)

    browser.find_element(By.TAG_NAME, "select").click()                 # open the dropdown list
    browser.find_element(By.CSS_SELECTOR, (f"[value='{z}']")).click()   # select the calculated number


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.execute_script("document.title='Script executing';alert('Robots at work');")            # execute_script method, show alert
    time.sleep(3)
    browser.quit()



