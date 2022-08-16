from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

link = "http://suninjuly.github.io/find_link_text"
secret_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, (secret_link))
    # or link = browser.find_element(By.LINK_TEXT, '224592')
    # or link = browser.find_element(By.LINK_TEXT, (str(math.ceil(math.pow(math.pi, math.e)*10000))))
    print(link)
    link.click()




    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("John")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Doe")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Seattle")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("U.S.")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций и в конце оставляем пустую строку 
    browser.quit()



