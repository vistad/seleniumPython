# this shows how the test file accesses the fixture "browser" in file conftest.py
# pytest -s -v test3_6_4conftest.py

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
