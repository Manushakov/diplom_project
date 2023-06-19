import os
import sys
import pytest
sys.path.insert(0, os.getcwd() + "\\framework\\")
from browser.check_browser import CheckBrowser
from tests.config.browser import BrowserConfig
from utils.checklogger import CheckLogger


def pytest_addoption(parser):
    parser.addoption("--login", action="store", help="Name of browser")
    parser.addoption("--password", action="store", help="Name of browser")


@pytest.fixture(scope="function")
def create_browser(request):
    credential = [request.config.getoption('--login'), request.config.getoption('--password')]
    CheckLogger()
    CheckBrowser(BrowserConfig.BROWSER, BrowserConfig.LOCALE)

    yield credential

    CheckBrowser.quit()


@pytest.fixture(scope="session", autouse=True)
def make_report():
    with open("allure-results/environment.properties", "w") as f:
        f.write(f'''Browser={BrowserConfig.BROWSER}\nBrowser.Version={BrowserConfig.CHROME_VERSION}''')
