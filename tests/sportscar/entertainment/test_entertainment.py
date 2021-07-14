from pytest import mark


@mark.entertainment
def test_entertainment_functions_as_expected():
    assert True

@mark.ui
@mark.entertainment
def test_can_navigate_to_audio_page(browser_chrome):
    browser_chrome.get('https://www.sony.com.ar/electronics/equipo-audio-sonido-auto-multimedia')
    assert True
