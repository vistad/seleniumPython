# the location of this file is: project/conftest.py
# there must not be other conftest.py files above

# the fixture to choose between chrome and gecko driver for tests
# pytest -s -v test_parser.py                           fails
# pytest -s -v --browser_name=chrome test_parser.py     passes
# pytest -s -v --browser_name=firefox test_parser.py    passes

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    print("\nquit browser..")
    yield browser
    browser.quit()


"""
# the location of this file is: top_directory/conftest.py
# the fixture to start chrome driver for tests

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    print("\nquit browser..")
    yield browser
    browser.quit()

"""


