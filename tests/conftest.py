import json

from pytest import fixture
from selenium import webdriver
from config import config


@fixture(scope='function')
def browser_chrome():
    browser = webdriver.Chrome()
    yield browser

    # Teardown
    print('Im tearing down this browser')


@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()


def pytest_addoption(parser):
    parser.addoption('--env',
        action ='store',
        help = 'Enviroment to run tests against'
        # default='dev'
    )


@fixture(scope='session')
def env(request):
    print(request.config.getoption("--env"))
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = config(env)
    return cfg


data_path = "D:/Repositorios/python-pytest-course/tests/test_data.json"


def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data
