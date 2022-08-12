# marks should be registered in pytest.ini file
# the inversion command to start all tests except for e.g. smoke or regression
# otherwise OR can be used, like smoke or regression
# pytest -v -s -m "not smoke" ~/seleniumPy/seleniumPython/test3_5_2_marks.py
# pytest -v -s -m "not regression" ~/seleniumPy/seleniumPython/test3_5_2_marks.py
# pytest -v -s -m "smoke or regression" ~/seleniumPy/seleniumPython/test3_5_2_marks.py

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


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
