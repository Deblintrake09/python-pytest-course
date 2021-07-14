from pytest import mark


# pytest -m engine tests only those marked as engine
# pytest -m "engine or entertainment"  tests those marked as engine OR entertainment

@mark.smoke
@mark.engine
def test_engine_functions_as_expected():
    assert True

@mark.ui
@mark.entertainment
def test_can_navigate_to_engine_page(browser_chrome):
    browser_chrome.get('https://www.energy.gov/eere/vehicles/articles/internal-combustion-engine-basics')
    assert True