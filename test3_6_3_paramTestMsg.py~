# pytest -s -v ~/seleniumPy/seleniumPython/test_3_6_2_parametrizeClass.py
# The owls are not what they seem! OvO

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

expected_result = 'Correct!'


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    print("\nmessage")
    print("\nquit browser..")
    yield browser
    browser.quit()

class TestMessage:

    @pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ])

    def test_feedback(self, browser, link):
            browser.get(link)
            browser.implicitly_wait(15)                  #wait for page to load
            browser.find_element(By.CSS_SELECTOR, "textarea.textarea").send_keys(str(math.log(int(time.time())))) 
            browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
            actual_result = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint ").text
            assert (actual_result == expected_result), f"expected '{expected_result}', got '{actual_result}'"





