import time
from pytest import mark


@mark.body
class BodyTests:

    @mark.door
    def test_body_functions_as_expected(self):
        assert True

    def test_bumper(self):
        assert False

    def test_windshield(self):
        assert False

    @mark.ui
    def test_can_navigate_to_body_page(self, browser_chrome):
        browser_chrome.get('https://auto-bodyparts.com/')

        time.sleep(5)
        second_browser = browser_chrome
        second_browser.get('https://github.com/')  #second call will open in the same window as first call one instance per function
        assert True
