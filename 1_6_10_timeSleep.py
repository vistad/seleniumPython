from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try: 
    link = "http://suninjuly.github.io/registration1.html"
    # link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # fill in the fields

    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input1.send_keys('John')

    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input2.send_keys('Doe')

    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    input3.send_keys('11111@email.com')



    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)           # wait for the page to load

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")          # find the text
    welcome_text = welcome_text_elt.text            # write the text from element welcome_text_elt to the var welcome_text

    assert "Congratulations! You have successfully registered!" == welcome_text         # check that expected text is the same as the page text using assert 

finally:
    time.sleep(10)
    browser.quit()


