# Открыть страницу http://SunInJuly.github.io/execute_script.html
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать кнопку "Submit"


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
 

    fnum = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(fnum.text)
    y = calc(x)
    print(x)
    print(y)


    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    robox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    robox.click()

    button = browser.find_element(By.TAG_NAME, ("button"))
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)     # execute_script

    robtn = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    robtn.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()



