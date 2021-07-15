from pytest import mark

@mark.config
@mark.xfail(reason='Env is not QA')
def test_enviroment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://myqa-env.com'
    assert port == 80

@mark.config
@mark.xfail(reason='Env is not DEV')
def test_enviroment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydev-env.com'
    assert port == 8080


@mark.skip(reason="broken by deploy number XXXX")
def test_enviroment_is_staging(app_config):
        base_url = app_config.base_url
        assert base_url == 'staging'


@mark.skip(reason='Broken. Fix next sprint')
def test_this_needs_more_work():
    assert False
