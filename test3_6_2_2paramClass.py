# pytest -s -v test3_6_2_2paramClass.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    print("\nquit browser..")
    yield browser
    browser.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])   #parametrize class
class TestLogin:

    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        # this test will run 2 times

    def test_guest_should_see_navbar_element(self, browser, language):
        # this test will run 2 times
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")


