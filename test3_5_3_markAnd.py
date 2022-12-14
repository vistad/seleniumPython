# marks should be registered in pytest.ini file
# Select and run only specific tests
# e.g. to run smoke-tests only for Windows 10, use logic AND:
# pytest -s -v -m "smoke and win10" test3_5_3_markAnd.py
# it will run test_guest_should_see_basket_link_on_the_main_page

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    print("\nquit browser..")
    yield browser
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    # smoke and win10
    @pytest.mark.smoke
    @pytest.mark.win10      
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

