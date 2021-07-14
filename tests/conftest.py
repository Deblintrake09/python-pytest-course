from pytest import fixture
from selenium import webdriver

@fixture(scope='function')
def browser_chrome():
    browser = webdriver.Chrome()
    yield browser

    # Teardown
    print('Im tearing down this browser')

