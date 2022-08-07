from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    button = browser.find_element(By.TAG_NAME, ("button"))
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()



