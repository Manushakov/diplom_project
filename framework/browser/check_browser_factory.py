from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


class CheckBrowserFactory:
    @staticmethod
    def get_driver(name, locale):
        serializer = CheckBrowserFactory._get_serializer(name)
        return serializer(locale)

    @staticmethod
    def _get_serializer(name):
        if name == "chrome":
            return CheckBrowserFactory.serialize_to_google

        if name == "firefox":
            return CheckBrowserFactory.serialize_to_firefox
        else:
            raise Exception("browser not found")

    @staticmethod
    def serialize_to_google(locale):
        chrome_options = ChromeOptions()
        chrome_options.add_argument(f"--lang={locale}")
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        browser.maximize_window()
        return browser

    @staticmethod
    def serialize_to_firefox(locale):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', locale)
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)
        browser.maximize_window()
        return browser
