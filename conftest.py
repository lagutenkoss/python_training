import pytest
from fixture.application import Application
import json



fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    if target is None:
        with open(request.config.getoption('--target')) as config_file:
            target = json.load(config_file)
    # baseUrl = request.config.getoption('--baseUrl')
    # password = request.config.getoption('--password')
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseUrl=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default="target.json")
    # parser.addoption('--baseUrl', action='store', default="http://localhost/addressbook/")
    # parser.addoption('--password', action='store', default='secret')
